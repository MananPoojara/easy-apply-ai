# Setup, portability and optional hooks

Install this folder as an Agent Skill using the host's supported mechanism. For Codex, copy or link the entire `easy-apply-ai` folder into `~/.codex/skills/easy-apply-ai` and start a new session; preserve all sibling files. Other hosts use their own documented skill location. Review the skill before installing and do not publish private search workspaces with it.

Agent Reach is optional: if it is installed, read its skill and run its health check before using the appropriate backend. If it is absent and the user wants it, consult the official project and host-specific installer before making changes: https://github.com/Panniantong/Agent-Reach. Never assume a command or configuration works on every host. Do not transfer browser profiles or restart an existing browser without the user's permission.

## Optional preflight hook

`scripts/preflight.py` is a read-only tracker preflight. Run it manually with `python3 <skill>/scripts/preflight.py <tracker.csv>`. It reports status totals and possible duplicates; it cannot prove submission or send applications. If the host supports hooks, the user can wire this exact command to a session-start or pre-run hook using that host's documented configuration. Hook interfaces differ by runtime: inspect current documentation and existing configuration, obtain the user's approval for configuration changes, and merge rather than replace. Do not install a hook automatically or block unrelated work. No hook can create a recurring run; configure and verify a supported scheduler separately when the user requests automation.
