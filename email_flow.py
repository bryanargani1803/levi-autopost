"""Gumroad -> Brevo follow-up emails. Runs hourly in GitHub Actions.
1. Pulls new Gumroad sales (free + paid) and adds each buyer to the Brevo list "Levi customers".
2. Sends the next email of their sequence when it is due (Brevo transactional API, free plan = 300/day).
   free product  -> 4 emails over 6 days ending with the bundle offer
   paid pack     -> 2 emails: setup tip, then the upgrade to the bundle
   bundle buyer  -> sequence stops (they already have everything)
Secrets: GUMROAD_TOKEN, BREVO_API_KEY. State lives in Brevo contact attributes (no emails stored in this public repo).
"""
import json, os, sys, urllib.request, urllib.parse, datetime as dt

GT, BK = os.environ.get("GUMROAD_TOKEN"), os.environ.get("BREVO_API_KEY")
LIST_NAME = "Levi customers"
NOW = dt.datetime.now(dt.timezone.utc)


def req(url, method="GET", body=None, headers=None):
    r = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                               headers={"Content-Type": "application/json", "Accept": "application/json", **(headers or {})})
    try:
        with urllib.request.urlopen(r, timeout=60) as f:
            t = f.read(); return json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        msg = e.read().decode()[:300]
        if e.code in (400,) and "already exist" in msg.lower(): return {}
        raise RuntimeError(f"{method} {url.split('?')[0]} -> {e.code} {msg}")


def brevo(path, method="GET", body=None):
    return req("https://api.brevo.com/v3" + path, method, body, {"api-key": BK})


def gumroad_sales(since):
    out, page = [], None
    while True:
        qs = {"access_token": GT, "after": since}
        if page: qs["page_key"] = page
        d = req("https://api.gumroad.com/v2/sales?" + urllib.parse.urlencode(qs))
        out += d.get("sales", [])
        page = d.get("next_page_key")
        if not page: return out


def setup():
    for name, typ in (("LV_SEQ", "text"), ("LV_STEP", "float"), ("LV_START", "date"), ("LV_BUNDLE", "boolean")):
        try: brevo(f"/contacts/attributes/normal/{name}", "POST", {"type": typ})
        except RuntimeError as e:
            if "exist" not in str(e).lower(): print("attr", name, e)
    lists = brevo("/contacts/lists?limit=50").get("lists", [])
    for l in lists:
        if l["name"] == LIST_NAME: return l["id"]
    folders = brevo("/contacts/folders?limit=10").get("folders", [])
    fid = folders[0]["id"] if folders else brevo("/contacts/folders", "POST", {"name": "Levi"})["id"]
    return brevo("/contacts/lists", "POST", {"name": LIST_NAME, "folderId": fid})["id"]


def classify(sale):
    p = (sale.get("product_permalink") or sale.get("permalink") or "").lower()
    name = (sale.get("product_name") or "").lower()
    if "all-access" in p or "all-access" in name: return "bundle"
    price = sale.get("price", 0) or 0
    return "free" if int(price) == 0 else "pack"


def import_sales(list_id):
    since = (NOW - dt.timedelta(days=3)).strftime("%Y-%m-%d")
    n = 0
    for s in gumroad_sales(since):
        email = (s.get("email") or "").strip().lower()
        if not email or s.get("refunded"): continue
        seq = classify(s)
        try:
            c = brevo("/contacts/" + urllib.parse.quote(email))
            a = c.get("attributes", {})
        except RuntimeError:
            a = None
        if a is None:
            brevo("/contacts", "POST", {"email": email, "listIds": [list_id], "updateEnabled": True,
                  "attributes": {"LV_SEQ": seq, "LV_STEP": 0, "LV_START": NOW.strftime("%Y-%m-%d"), "LV_BUNDLE": seq == "bundle"}})
            n += 1
        elif seq == "bundle" and not a.get("LV_BUNDLE"):
            brevo("/contacts/" + urllib.parse.quote(email), "PUT", {"attributes": {"LV_BUNDLE": True}})
        elif seq == "pack" and a.get("LV_SEQ") == "free":  # upgraded from free to a pack: switch sequence
            brevo("/contacts/" + urllib.parse.quote(email), "PUT", {"attributes": {"LV_SEQ": "pack", "LV_STEP": 0, "LV_START": NOW.strftime("%Y-%m-%d")}})
    print("new contacts:", n)


def send_due(list_id, emails, sender, footer):
    offset, sent = 0, 0
    while True:
        d = brevo(f"/contacts/lists/{list_id}/contacts?limit=500&offset={offset}")
        cs = d.get("contacts", [])
        for c in cs:
            a = c.get("attributes", {})
            if c.get("emailBlacklisted") or a.get("LV_BUNDLE"): continue
            seq, step = a.get("LV_SEQ"), int(a.get("LV_STEP") or 0)
            if seq not in emails or step >= len(emails[seq]) or not a.get("LV_START"): continue
            e = emails[seq][step]
            start = dt.datetime.strptime(a["LV_START"][:10], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
            if NOW < start + dt.timedelta(days=e["day"]): continue
            brevo("/smtp/email", "POST", {"sender": sender, "to": [{"email": c["email"]}], "subject": e["subject"],
                  "htmlContent": e["html"] + footer, "tags": [f"{seq}-{step}"]})
            brevo("/contacts/" + urllib.parse.quote(c["email"]), "PUT", {"attributes": {"LV_STEP": step + 1}})
            sent += 1
            if sent >= 250: print("daily cap reached"); return
        offset += 500
        if len(cs) < 500: break
    print("emails sent:", sent)


def main():
    if not (GT and BK): sys.exit("Missing GUMROAD_TOKEN or BREVO_API_KEY secret")
    acc = brevo("/account")
    addr = acc.get("address", {})
    sender = {"email": os.environ.get("SENDER_EMAIL") or acc["email"], "name": "Levi"}
    place = ", ".join(x for x in (addr.get("street"), addr.get("city"), addr.get("zipCode"), addr.get("country")) if x)
    footer = (f'<p style="color:#888;font-size:12px;margin-top:32px">You got this because you downloaded something from '
              f'levitheblue.gumroad.com. Don\'t want these? Reply "stop" or <a href="mailto:{sender["email"]}?subject=unsubscribe">unsubscribe</a>.'
              f'<br>{place}</p>')
    list_id = setup()
    import_sales(list_id)
    send_due(list_id, json.load(open("emails.json")), sender, footer)


if __name__ == "__main__":
    main()
