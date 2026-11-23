# easy-apply-ai

A reusable agent skill for candidate intake, evidence-based job research, tailored applications and outcome tracking. It contains no candidate data or credentials.

For Codex, copy the entire `easy-apply-ai` directory to `~/.codex/skills/easy-apply-ai` and start a new session. Invoke it with `$easy-apply-ai`. Other agent hosts can install the folder using their own Agent Skills instructions. Read [SKILL.md](SKILL.md) before use; setup and optional hooks are in [references/setup-and-hooks.md](references/setup-and-hooks.md).

The skill first resumes from conversation, profile, résumé, tracker, and connected context; it asks only for missing application-critical facts. It can delegate a bounded job-search lane to a subagent when the host supports delegation and a higher-priority task is active. The parent remains accountable for reconciliation and final counts. It maintains a small pointer in the chosen workspace's `AGENTS.md` only when compatible with existing instructions. It does not install a scheduler or send applications merely by being installed. Agent Reach, connectors, browser tools, delegation, and hooks depend on the host and available permissions.
