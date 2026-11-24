"""Daily auto-poster: takes the next posts from queue.json and adds them to Buffer.
Runs in GitHub Actions. Needs repo secret BUFFER_API_KEY.
Posts go to every connected X (twitter), Threads, Bluesky and LinkedIn channel.
"""
import json, os, sys, urllib.request

API = "https://api.buffer.com"
KEY = os.environ.get("BUFFER_API_KEY")
PER_DAY = int(os.environ.get("POSTS_PER_DAY", "3"))
SERVICES = {"twitter", "threads", "bluesky", "linkedin"}


def gql(query, variables=None):
    req = urllib.request.Request(API, data=json.dumps({"query": query, "variables": variables or {}}).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {KEY}",
                                          "User-Agent": "levi-autopost"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.loads(r.read())
    if out.get("errors"):
        raise RuntimeError(out["errors"])
    return out["data"]


def channels():
    orgs = gql("query { account { organizations { id name } } }")["account"]["organizations"]
    chs = []
    for o in orgs:
        q = "query($id: OrganizationId!) { channels(input: { organizationId: $id }) { id name service } }"
        try:
            chs += gql(q, {"id": o["id"]})["channels"]
        except Exception:
            q2 = 'query { channels(input: { organizationId: "%s" }) { id name service } }' % o["id"]
            chs += gql(q2)["channels"]
    return [c for c in chs if c["service"] in SERVICES]


CREATE = """mutation($input: CreatePostInput!) { createPost(input: $input) {
  ... on PostActionSuccess { post { id dueAt } }
  ... on MutationError { message } } }"""


def fill(text, q):
    return text.replace("{vault}", q["vault"]).replace("{bundle}", q["bundle"]).replace("{repo}", q["repo"])


def main():
    if not KEY:
        sys.exit("BUFFER_API_KEY secret is missing")
    q = json.load(open("queue.json"))
    st = json.load(open("state.json")) if os.path.exists("state.json") else {"post": 0, "thread": 0, "day": 0}
    chs = channels()
    print("channels:", [(c["service"], c["name"]) for c in chs])
    items = []
    for _ in range(PER_DAY):
        if st["post"] < len(q["posts"]):
            items.append(("post", fill(q["posts"][st["post"]]["t"], q))); st["post"] += 1
    if st["day"] % 2 == 0 and st["thread"] < len(q["threads"]):  # a thread every 2nd day
        items.append(("thread", [fill(t, q) for t in q["threads"][st["thread"]]])); st["thread"] += 1
    st["day"] += 1
    if not items:
        print("Queue empty - ask Claude for the next batch."); return
    for kind, body in items:
        for c in chs:
            inp = {"channelId": c["id"], "schedulingType": "automatic", "mode": "addToQueue"}
            if kind == "post":
                inp["text"] = body[:280] if c["service"] == "twitter" else body
            else:
                inp["text"] = body[0]
                if c["service"] in ("twitter", "threads", "bluesky"):
                    inp["metadata"] = {c["service"]: {"thread": [{"text": t} for t in body]}}
                else:
                    inp["text"] = "\n\n".join(body)
            try:
                print(kind, c["service"], gql(CREATE, {"input": inp})["createPost"])
            except Exception as e:
                print("FAILED", kind, c["service"], e)
    json.dump(st, open("state.json", "w"))


if __name__ == "__main__":
    main()
