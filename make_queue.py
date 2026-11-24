"""Builds queue.json v2: posts built on the proven X templates (Alex/Adam/affprinter), adapted to Claude Skills.
cta: None = pure value (bookmark bait), "SKILLS" = free vault, "108" = bundle, "SLOP" = free anti-slop skill.
On X the CTA is comment-a-word (you DM by hand). On Threads/Bluesky/LinkedIn the CTA is the direct link.
"""
import json

P = []
def add(cta, t): P.append({"cta": cta, "t": t.strip()})

# ---------- DAY 1 ----------
add("SKILLS", """
You're cooked in 2026 if you still open Claude and type the same prompt you typed yesterday.

The people getting 10x more out of it stopped prompting.

They write the process down once, as a Skill, and Claude runs it by itself every time the task shows up:

› the email reply that sounds like them
› the meeting notes in their format
› the weekly plan
› the research brief
› the post that doesn't read like AI

One markdown file each. No code. 2 minutes to install.

I packaged 10 of mine into a free Starter Vault.
""")
add(None, """
A Claude Skill is one markdown file with 6 parts:

1. name
2. description (when Claude should use it)
3. what to ask you first
4. the steps, numbered
5. the output format
6. the rules (what never to do)

Get #2 right and Claude loads it on its own. Get it wrong and it never fires.

Save this.
""")
add(None, """
Prompt = you remember the process.
Skill = Claude remembers the process.

That's the whole difference. And it's why one is a habit and the other is a system.
""")
# ---------- DAY 2 ----------
add("108", """
I spent 3 weeks writing 108 Claude Skills that do the boring half of running an online business.

Not "prompts". Full workflows Claude follows step by step:

› Content: hooks, threads, LinkedIn, 30-day calendar
› Email: welcome sequence, launches, free-to-paid
› Sales: Gumroad page, objections, 7-day launch
› Outreach: cold email, follow-ups, DMs
› SEO: keyword clusters, briefs, full articles
› Products: demand finder, validator, ebook outliner
› Video: faceless scripts, storyboards, captions
› Claude Code + n8n: tools and automations for non-coders

Each one comes with a ChatGPT/Gemini prompt version too.

Founder price is live for the first buyers.
""")
add(None, """
The #1 reason a Claude Skill never triggers: the description is a label, not a trigger.

Bad:
"Helps with marketing."

Good:
"Use when the user asks for opening lines, hooks or first sentences for a post, or says their posts get no reach."

Write the situations and the exact words people say. Claude matches on those.
""")
add(None, """
Stop asking Claude to "write a post."

Ask it to:
1. write 15 hooks across 5 formulas
2. score each one 1-10 for curiosity and clarity
3. show the top 3 with the reason they win

Same 30 seconds. You never post a weak first line again.
""")
# ---------- DAY 3 ----------
add("SLOP", """
Words that make people stop reading because they smell AI:

delve
elevate
unlock
seamless
game-changer
"in today's fast-paced world"
"it's not just X, it's Y"
"let's dive in"
three-item lists in every sentence
an em dash every other line

I made a free Claude Skill that finds and rewrites all of them before you hit post.
""")
add(None, """
Claude Skills break in a predictable order:

1. Description too vague → never loads
2. No "ask first" step → guesses your context
3. Steps written as paragraphs → skips half
4. No output format → different shape every time
5. No examples → generic tone
6. No "never do" rules → AI-sounding filler
7. Too many jobs in one skill → does none well
8. No voice file → doesn't sound like you

Fix them in that order. Bookmark it.
""")
add(None, """
The best Claude users I know have the most boring setup:

a folder of 20-30 small skills that each do one job well.

Not one giant "do everything" prompt.
""")
# ---------- DAY 4 ----------
add("SKILLS", """
If I had to get 10 hours a week back with Claude, starting tonight, here's exactly what I'd do:

1. List every task I did twice this week
2. Pick the 3 that take the longest
3. Write each one as a Skill: ask first → steps → output format → rules
4. Add one example of a great past result to each
5. Run it on real work, fix the rule that broke
6. Repeat with the next 3 next week

By week 4 Claude runs the busywork the same way every time.

I already wrote the first 10 for you (email replies, meeting notes, weekly plan, research briefs, rewrites and more). Free.
""")
add(None, """
How to make Claude sound like you (2 steps):

1. Paste 5 things you wrote and liked. Ask: "Describe my voice in 10 rules: sentence length, words I use, words I never use, how I open, how I close."

2. Save those 10 rules as a voice profile and tell every writing skill to read it first.

That's the whole trick. Most people skip step 2.
""")
add(None, """
Claude doesn't need a better prompt from you.

It needs your process, written down once.
""")
# ---------- DAY 5 ----------
add("108", """
Claude Skills are honestly the most underrated AI feature of 2026, by far.

› You write a workflow once
› Claude picks it up by itself when the task comes up
› Works in the Claude app, Claude Code and the API
› It's a plain text file you own, not a paid tool

Most people still don't know the button exists.

I built 108 of them for creators and solo businesses: content, email, sales pages, outreach, SEO, digital products, faceless video, n8n and Claude Code.
""")
add(None, """
The 5 Claude Skills I'd install first if I ran a one-person business:

1. Email reply in my voice
2. Meeting/call notes → action list
3. Weekly plan from a brain dump
4. Research brief on any topic in 10 minutes
5. "Make this clear" rewrite for anything I send

None of them are exciting. All of them run every day.
""")
add(None, """
A Skill without an example is a guess.

Paste one great past result inside the skill and write "match this quality and length."

The difference is bigger than any model upgrade.
""")
# ---------- DAY 6 ----------
add("SKILLS", """
You can build your own AI assistant with one folder of text files and nobody talks about how simple it is.

No agents. No code. No subscriptions on top of Claude.

› skill 1 answers your emails in your voice
› skill 2 turns call notes into tasks
› skill 3 plans your week
› skill 4 writes research briefs
› skill 5 rewrites anything to be clear

Claude reads the folder and picks the right one for the task.

Here are my first 10, free.
""")
add(None, """
Copy this into any Claude Skill and the output instantly gets better:

## Rules
- Ask before assuming anything about my audience or goal
- Short sentences. One idea per line.
- No words: delve, elevate, unlock, seamless, leverage
- No intro, no summary at the end
- If something is missing, say so instead of making it up
""")
add(None, """
Most "AI is useless" takes come from people who never gave it the context a new hire would get on day one.
""")
# ---------- DAY 7 ----------
add("108", """
If I had to start selling a digital product this week, with no audience and only Claude, here's the exact order:

1. Find the demand: 20 complaints people already post (Reddit, X, reviews)
2. Validate: does one product fix 3 of them?
3. Build the offer: outcome, bonuses, price anchor
4. Outline and write it in chapters, not one giant prompt
5. Gumroad page: headline, bullets, FAQ that kills objections
6. 7-day launch: one post a day, one email a day
7. Upsell: checkout add-on and a bundle

Every step above is a Claude Skill in my bundle (108 total).
""")
add(None, """
The hook formula that works on every platform:

[number or name] + [surprising claim] in under 15 words.
Then one short line.
Then white space.
Then a list.

Look at the posts you saved this month. Almost all of them follow it.
""")
add(None, """
Reply under bigger accounts with something they'd want to retweet.

That's the whole cold-start growth strategy for 0 followers. Everything else is optimization.
""")
# ---------- DAY 8 ----------
add("SKILLS", """
I tested every way to "save prompts" for Claude:

› notes app → forget to open it
› text expander → still edit every time
› Projects → good, but stuck in one chat
› custom instructions → too general

Skills won.

Claude loads the right one on its own, follows the same steps every time and asks you the questions you'd forget.

Start with my 10 free ones.
""")
add(None, """
The research-brief skill I use before writing anything:

1. Ask me: topic, who it's for, what decision it should help with
2. List what's known, what's debated, what's changed this year
3. 5 facts with sources I can check
4. 3 angles nobody is talking about
5. One paragraph: "if you read nothing else"

10 minutes instead of 2 hours of tabs.
""")
add(None, """
"Write me a blog post" gets you a blog post.

"Here are my steps for a blog post" gets you YOUR blog post.
""")
# ---------- DAY 9 ----------
add("SLOP", """
Run any AI-written post through this checklist. Most fail at least 4:

1. Opens with "In today's world…"
2. Uses "delve", "unlock" or "elevate"
3. "It's not just X, it's Y"
4. Three adjectives in a row
5. Ends with a question nobody will answer
6. Every paragraph the same length
7. No specific number, name or example

I made a free Claude Skill that fixes all 7.
""")
add(None, """
How to make Claude write a 30-day content calendar you'll actually use:

1. Give it 3 content pillars (what you know, what you sell, what you believe)
2. Ask for 4 formats: list, story, how-to, opinion
3. Pillars × formats = 12 ideas, repeat with new angles
4. Ask for the hook only, not the full post
5. Write the post the day you publish it

Planning the hooks is 80% of the work.
""")
add(None, """
If your prompt is longer than 3 paragraphs and you use it more than once, it should be a Skill.
""")
# ---------- DAY 10 ----------
add("108", """
The full stack of Claude Skills I'd want if I sold anything online:

Content Engine: 12
Email Marketing: 12
Sales Page & Launch: 12
Cold Outreach: 12
SEO Blog Writer: 12
Digital Product Creator: 12
Faceless Video: 12
Claude Code for Non-Coders: 12
Claude + n8n Automations: 12

108 skills. Each with a ChatGPT/Gemini prompt version.

All 9 packs in one bundle, founder price for the first buyers.
""")
add(None, """
Cold email that gets replies, as a Claude Skill:

1. Ask me: who they are, one specific thing about them, what I offer
2. First line: about them, not me
3. One sentence problem, one sentence result
4. Ask for a 1-word reply, not a call
5. Under 80 words
6. Never: "I hope this finds you well"

Save it as a skill once, run it on every lead.
""")
add(None, """
The reason your AI posts get no reach isn't the algorithm.

It's that they sound like everyone else's AI posts.
""")
# ---------- DAY 11 ----------
add("SKILLS", """
Things Claude can do every day without you re-explaining anything (once you set up Skills):

› reply to emails in your tone
› turn a messy call into 5 action items
› build next week's plan from a brain dump
› write a research brief with sources
› rewrite anything so a 12-year-old gets it
› give you 30 content ideas from one topic
› turn any rough prompt into a strong one
› make a new skill from a task you describe

The last one builds the rest.

All 8 (plus 2 more) are in my free Starter Vault.
""")
add(None, """
The skill that builds other skills (use it first):

"I'll describe a task I repeat. Ask me 5 questions about it. Then write a SKILL.md with: name, a description listing the exact phrases that should trigger it, ask-first questions, numbered steps, output format and 5 'never do' rules."

Run it on your 3 most repeated tasks today.
""")
add(None, """
2024: learn prompting.
2025: learn agents.
2026: write your process down once and let Claude run it.
""")
# ---------- DAY 12 ----------
add("108", """
You can run the marketing side of a one-person business with 9 folders of Claude Skills and nobody talks about it.

› Monday: content calendar skill → 7 hooks
› Tuesday: thread + LinkedIn skills → posts done
› Wednesday: newsletter skill → email out
› Thursday: cold email skill → 20 leads
› Friday: SEO skill → 1 article
› Weekend: product skills → next offer outlined

The work doesn't disappear. The blank page does.

I built all 108 of these skills. One bundle.
""")
add(None, """
How to make Claude write an email welcome sequence in 10 minutes:

Email 1: deliver what they signed up for + one quick win
Email 2: your story in 5 lines, why you made this
Email 3: the most common mistake in your niche
Email 4: a case or example, with numbers
Email 5: the offer, one link, a deadline

Ask Claude for one email at a time. Never all 5 at once.
""")
add(None, """
Claude Code isn't only for developers.

Non-coders use it to build landing pages, Chrome extensions, small tools and automations, by describing what they want in plain English.
""")
# ---------- DAY 13 ----------
add("SKILLS", """
If I was starting with Claude from zero today, I'd skip every course and do this in one evening:

1. Install 10 ready-made Skills
2. Use each one once on real work
3. Open the file and read how it's written
4. Change one rule so it fits you
5. Use the "skill maker" to write your first own skill

You learn faster from 10 working examples than from 10 hours of video.

My 10 are free.
""")
add(None, """
A Gumroad sales page structure Claude can fill in for any product:

1. Headline: the result + the time it takes
2. Who it's for (and who it isn't)
3. What's inside, as outcome bullets
4. Why it works / what's different
5. Bonuses
6. FAQ that answers the 5 objections
7. Price + one reason to buy today

Feed it your product notes. Edit the headline yourself.
""")
add(None, """
Give Claude your process and it gets better every month as the models get better.

Give it random prompts and you start from zero every time.
""")
# ---------- DAY 14 ----------
add("108", """
I put every Claude Skill I built into one place:

108 skills. 9 packs. One bundle.

› What you get: 108 SKILL.md files + ChatGPT/Gemini prompt versions
› Install: drag the folder into Claude, 2 minutes
› Works with: Claude app, Claude Code, API
› Who it's for: creators, freelancers, solo founders, anyone selling online

Founder price for the first buyers, then it goes up.
""")
add(None, """
Free Claude Skills worth installing today:

› anti-AI-slop editor
› hook writer
› n8n workflow planner
› cold email writer
› headline lab
› idea validator

All open on my GitHub: {repo}
""")
add(None, """
The skill is the asset. The prompt was just the draft.
""")

T = [
 ["How to build your first Claude Skill in 20 minutes (no code):",
  "1/ Pick a task you did twice this week. Writing a reply, summarising a call, planning a post. Small and boring is perfect.",
  "2/ Open a new file called SKILL.md. At the top write a name and a description. The description is the trigger: list the situations and the exact words someone would say.",
  "3/ Add an 'Ask first' section: the 3 questions Claude should ask before starting. This is what stops generic output.",
  "4/ Write the steps as a numbered list. One action per line. If a step needs judgment, add the rule for it.",
  "5/ Add the output format. Headings, length, bullet or prose. Claude copies the shape you give it.",
  "6/ Add 'Never' rules: words to avoid, things not to assume, what to do when info is missing.",
  "7/ Paste one great past example and write 'match this quality'.",
  "8/ Zip the folder and upload it in Claude settings → Skills. Done.",
  "If you want 10 finished examples to copy from, they're free here: {vault}"],
 ["10 Claude Skills every creator should have (steal the structure):",
  "1/ Voice profile: 10 rules that describe how you write. Every other skill reads it first.",
  "2/ Hook writer: 15 hooks across 5 formulas, scored, top 3 explained.",
  "3/ Thread builder: one idea → 8 posts, each one standalone.",
  "4/ Repurposer: one long post → LinkedIn, Threads, X and a newsletter.",
  "5/ 30-day calendar: pillars × formats, hooks only.",
  "6/ Reply writer: replies to big accounts that add something, not 'great post'.",
  "7/ Carousel writer: 8 slides, one idea per slide.",
  "8/ Post audit: why a post flopped and the one thing to change.",
  "9/ Bio optimizer: who you help, with what, and proof.",
  "10/ Anti-slop editor: strips AI tells before you post.",
  "The full Content Engine pack (12 skills) is in the bundle: {bundle}"],
 ["I read through the most saved AI posts on X this month. 7 patterns they all share:",
  "1/ Line one has a number or a name in it.",
  "2/ Line two is one short sentence. Then white space.",
  "3/ The body is a list, not paragraphs.",
  "4/ Every item is specific enough to act on today.",
  "5/ No links in the post itself. Links go in the reply.",
  "6/ No hashtags.",
  "7/ It's complete. You could save it and never come back, and that's exactly why people save it.",
  "I turned these into a hook-writer skill. Free on GitHub: {repo}"],
 ["How to use Claude + n8n to automate the boring parts of your business (no code):",
  "1/ Describe the workflow in plain English: trigger, steps, where data ends up.",
  "2/ Ask Claude to turn it into n8n nodes, in order, with what each node needs.",
  "3/ Ask for the workflow JSON. Paste it into n8n. It imports as a full flow.",
  "4/ Add your API keys inside n8n (never paste them into the chat).",
  "5/ When it errors, paste the error and the node into Claude. Ask for the fix, not an explanation.",
  "6/ Ideas to start: new sale → spreadsheet + email, new lead → research brief, new video → posts.",
  "The 12 Claude + n8n skills I use are in the bundle: {bundle}"],
 ["Claude Skills vs Projects vs custom instructions. When to use which:",
  "1/ Custom instructions: who you are and how you like answers. Applies to everything. Keep it short.",
  "2/ Projects: a shared folder of files for one piece of work. Great for context, stuck in that project.",
  "3/ Skills: a process. Claude loads it in any chat, only when the task matches.",
  "4/ Rule of thumb: facts about you → instructions. Files about a project → Project. Steps you repeat → Skill.",
  "5/ Most people put processes in instructions. That's why their outputs drift.",
  "Starter set of 10 skills, free: {vault}"],
 ["The free-to-paid funnel I'd build with Claude in a weekend:",
  "1/ Free product that solves one small problem completely.",
  "2/ Delivery email with one quick win in the first 3 lines.",
  "3/ 4 emails over 7 days: story, mistake, example, offer.",
  "4/ The paid product picks up exactly where the free one stops.",
  "5/ Checkout add-on under $20 and a bundle as the upgrade.",
  "6/ Every post on social points to the free product, not the paid one.",
  "Every step is a skill in my Email Marketing and Sales Page packs: {bundle}"],
]

CTA_X = {
 "SKILLS": 'Like + repost, then comment "SKILLS" and I\'ll DM you the free vault.\n(Follow me so the DM goes through.)',
 "108": 'Like + repost, then comment "108" and I\'ll DM you the link with the founder price.\n(Follow me so the DM goes through.)',
 "SLOP": 'Like + repost, then comment "SLOP" and I\'ll DM it to you free.\n(Follow me so the DM goes through.)',
}
CTA_LINK = {"SKILLS": "Free here: {vault}", "108": "Founder price here: {bundle}", "SLOP": "Free here: {slop}"}

q = {"vault": "levitheblue.gumroad.com/l/claude-skills-free",
     "bundle": "levitheblue.gumroad.com/l/claude-skills-all-access/FOUNDER",
     "slop": "levitheblue.gumroad.com/l/anti-ai-slop",
     "repo": "github.com/bryanargani1803/claude-skills",
     "cta_x": CTA_X, "cta_link": CTA_LINK, "posts": P, "threads": T}
json.dump(q, open("queue.json", "w"), indent=1, ensure_ascii=False)
print(len(P), "posts,", len(T), "threads,", sum(1 for p in P if p["cta"]), "with CTA")
for p in P:
    n = len(p["t"]) + (len(CTA_X[p["cta"]]) + 2 if p["cta"] else 0)
    if n > 1500: print("long", n, p["t"][:40])
