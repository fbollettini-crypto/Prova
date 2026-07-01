---
name: outreach
description: Prepare Albert School partnership outreach to corporate executives. Use when asked to prospect, research, or draft partnership emails to companies or executives. Takes a list of targets (companies and/or named executives) as arguments.
---

# Partnership outreach run

Prepare partnership outreach for the targets given in the arguments. If no
targets were given, ask the user for a shortlist (companies and/or named
executives, ideally with a hint of why they're interesting) — do not invent
a target list yourself.

## Steps

1. **Parse the targets.** Cap the run at 15 prospects; if given more, take
   the first 15 and tell the user what was deferred.
2. **Confirm the sender identity** (name, role, email for the signature) if
   not already known from the conversation.
3. **Delegate each prospect** to the `partnership-outreach` agent (run
   independent prospects in parallel). The agent qualifies against HubSpot,
   researches the company and executive, drafts a personalized email from
   `templates/outreach-templates.md`, stages it as a Gmail draft, and logs
   the activity in HubSpot.
4. **Synthesize** the results into a single review table for the user:
   prospect, fit ranking, chosen angle, hook used (with source), draft
   location, and any prospects skipped (already in an active HubSpot
   conversation, or research found no plausible fit).

## Hard rules

- Emails are staged as drafts only. Never send, never schedule a send.
- Never fabricate recipient email addresses or facts about a prospect.
- Skip prospects with an active or recent (< 90 days) HubSpot conversation
  and report them instead.
