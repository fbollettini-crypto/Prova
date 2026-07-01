# Albert School — Corporate Partnership Outreach Agent

A Claude Code agent that researches corporate executives and prepares
personalized outreach proposing a partnership with Albert School. It is
deliberately **human-in-the-loop**: it qualifies, researches, and drafts —
a person always reviews and sends.

## What it does

For each prospect (a company or a named executive):

1. **Qualifies** — checks HubSpot for existing contacts and active
   conversations so nobody gets double-contacted.
2. **Researches** — builds a short brief from the web: company strategy,
   data/AI initiatives, the executive's role and public statements, and one
   verified hook to personalize the email.
3. **Drafts** — writes a sub-150-word email (FR or EN) from
   [`templates/outreach-templates.md`](templates/outreach-templates.md),
   proposing the partnership format that fits best: student business cases,
   talent pipeline (internships/alternance/hiring), executive education, or
   strategic sponsorship.
4. **Stages for review** — saves the email as a Gmail draft and logs the
   research and status in HubSpot. It never sends anything itself.

## How to use it

From a Claude Code session in this repo (with the Gmail and HubSpot MCP
servers connected):

```
/outreach LVMH (Chief Data Officer); CMA CGM; Doctolib (CTO)
```

or just describe what you want in plain language — e.g. *"prepare outreach
to the heads of data at three large French retailers"*. Claude will invoke
the `partnership-outreach` agent per prospect and return a review table with
each draft's location, angle, and sources.

Then review the Gmail drafts, edit as needed, and send the ones you approve.

## Repository layout

| Path | Purpose |
|---|---|
| `.claude/agents/partnership-outreach.md` | The agent: workflow, Albert School talking points, guardrails |
| `.claude/skills/outreach/SKILL.md` | The `/outreach` command that fans out over a target list |
| `templates/outreach-templates.md` | FR/EN email skeletons and per-angle variants |

## Guardrails (by design)

- Drafts only — no autonomous sending, replying, or scheduling.
- Max 15 prospects per run; blast-style requests are refused.
- No fabricated facts, hooks, or email addresses; every hook cites a source.
- Max 2 follow-ups per prospect, ≥ 7 days apart; opt-outs honored permanently.
- Skips anyone with an active or recent (< 90 days) HubSpot conversation.
