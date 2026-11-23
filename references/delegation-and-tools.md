# Delegation and tool routing

## Coordinator and worker contract

The coordinator owns the search state, user relationship, and final reporting. A worker is a bounded execution lane, not a separate source of truth. Start one only when the host supports subagents and the user has a higher-priority task to keep moving (or has otherwise requested delegation).

Give each worker:

- the skill path and this run's objective, constraints, timezone, daily target, and stop/checkpoint rule;
- paths to the existing candidate profile and tracker, plus the current confirmed status/count;
- standing application or communication authorization already granted, and explicit exclusions;
- a finite scope (for example, discover and verify up to five new consulting/trainer roles, then prepare candidate-specific materials);
- a write boundary: assigned tracker rows only; no profile changes; no simultaneous use of a shared account/browser.

The worker returns a concise handoff with role and employer, canonical job URL, source and checked date, eligibility/fit evidence, duplicate-check result, prepared/submitted status, confirmation evidence, blockers, and changed tracker rows. The coordinator reconciles the handoff and records the confirmed count. If the host lacks subagents, proceed in the active lane or leave a durable handoff; never claim an idle agent will keep working after the session.

For parallel batches, assign non-overlapping employers or tracker ranges. Before submission, check for duplicates again. Serialize Gmail/X sends and browser-form submissions if they share an account or session. A single coordinator should own the daily count and status reconciliation.

## Route by task and capability

1. Inspect available skills, MCP connectors, and tools first. Use a fit-for-purpose connected service when available; don't ask the user to reconnect something that is already available.
2. For public web, recruiting, job-post, and X/Twitter research, use `agent-reach` when installed. Read its skill, check its health/routing, use the documented backend for that channel, and obey rate limits and credential boundaries. Record the original employer posting, not only a search snippet. Social search is evidence discovery; do not interact with posts or people unless separately authorized.
3. For mail, use the connected Gmail capability to inspect relevant recruiter responses, application confirmations, sent messages, and delivery-status notifications. Search by employer/application context and date; distinguish a bounce from an employer rejection or a sent message. Do not forward private messages to unrelated services.
4. For X/Twitter DMs, use only an available authorized connector or the user's authorized session and the host's allowed interaction path. The user can authorize a class of tailored job-application messages; keep messages truthful and role-specific. Never treat public read access as permission to send.
5. For application pages, use an available browser automation skill or tool. Prefer an isolated task session. Do not restart the user's main browser, change profiles, or bypass access restrictions, rate limits, or human-verification challenges. If a challenge requires user action, pause that application and continue independent work.
6. Use local job-board CLIs or public feeds as additional discovery sources, not as proof of eligibility or current availability. Verify the employer's own posting before applying.

## Existing context and repeat questions

At each resume, gather the current conversation, prior handoff, existing candidate profile, résumé, tracker, relevant project evidence, and connected mailbox/profile context available to the host. Reuse confirmed facts and standing authorization. If sources conflict, prefer a recent direct user confirmation, then authoritative candidate documents, then older records; flag a material conflict instead of silently choosing. Ask only for a missing answer needed by a concrete application or required legal attestation. Ask once in a compact batch, and do not block unrelated research while awaiting it. Keep opinions, agreements, consent, and eligibility claims in the user's own voice unless the user explicitly authorized a truthful draft and confirmed its substance.

## Durable handoff

When a task must yield to a higher-priority task or the session may end, write a short handoff in the chosen private workspace: last verified local date/timezone and count, completed/confirmed work, prepared/unconfirmed items, replies/bounces, unresolved blockers, next safe action, and tracker location. Keep credentials and unnecessary personal data out of the handoff. A target of 50 applications is a quota goal, not permission to lower evidence standards or count drafts, attempts, retries, and bounces as successful submissions.
