<div align="center">

<img src="assets/calm-banner.png" alt="Easy Apply AI — AI-assisted job search" width="680" />

**A job search, guided by you and powered by your AI agent.**

Find relevant roles · Tailor honest applications · Keep track of what happens

[Get started](#get-started) · [Connect email](#3-connect-your-email) · [How it works](#how-it-works) · [Privacy](#privacy-and-control) · [Project structure](#project-structure)

</div>

---

Searching for a job takes more than clicking Apply. You need to find roles that fit, explain your experience clearly, follow different application routes, and remember where you left off. **Easy Apply AI** is a reusable agent skill that gives your assistant a practical workflow for that process.

Tell it what you want, share your résumé and preferences, and let it help you research opportunities, prepare tailored applications, submit within your authorization, and maintain a private tracker. It can resume from information you've already provided instead of starting intake from scratch.

## What it does

| | |
| --- | --- |
| **Learns your preferences** | Asks what work, problems, and missions interest you, then uses your résumé and projects to support your applications. |
| **Finds and screens opportunities** | Researches employer pages, job boards, and supported social sources; checks fit, location, and duplicates. |
| **Tailors each application** | Connects your real experience and projects to the role without inventing qualifications or accomplishments. |
| **Applies through available tools** | Uses supported browser, email, and other integrations when authorized and available in your agent host. |
| **Tracks what happened** | Records evidence, pending steps, replies, and delivery failures. A sent inquiry is not automatically a confirmed job application. |
| **Keeps momentum** | Works toward your target in batches and records a handoff when a step needs your input or the host cannot continue. |

## Get started

### 1. Install the skill

For Codex, clone this repository into your skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/MananPoojara/easy-apply-ai.git ~/.codex/skills/easy-apply-ai
```

Start a new Codex session, then invoke the skill:

```text
$easy-apply-ai Ask what kind of work I want, then help me set up my job search.
```

For other agent hosts, install this folder according to their Agent Skills instructions. The skill's instructions are in [SKILL.md](SKILL.md).

### 2. Start with what you want to do

Tell the agent what kind of work you want and why: the problems you want to solve, role families or causes you want to explore, preferred work setup, and work you want to avoid. Then share your résumé or its path, plus practical constraints such as location, compensation, and notice period. The agent uses your résumé to verify skills and experience and to tailor applications; it should not guess your interests from résumé keywords or let your past job titles decide your next move.

For example:

```text
$easy-apply-ai I want to explore remote junior AI consulting and AI-native engineering roles, including mission-driven organizations. I want to avoid senior and teaching jobs.
My résumé is at /path/to/resume.pdf. Target 20 applications today.
Use my existing profile and tracker, and ask if a required answer is missing.
```

The skill should search from those stated interests, then connect suitable openings to evidence in the résumé and projects. A résumé helps show what the person can do; the person sets the direction.

### 3. Connect your email

With a connected mailbox, the agent can check recruiter replies and delivery failures, look for previous applications, and send application emails when you authorize it.

1. **Codex desktop or ChatGPT:** Open **Plugins** or **Settings → Plugins**, find Gmail or Outlook Email, install it if prompted, and select **Connect**. In a Codex task view that shows **Sources → Use plugins**, select the installed plugin there.
2. **Claude Code:** Open [Claude connectors](https://claude.ai/customize/connectors), connect Gmail or Microsoft 365, then run `/mcp` in Claude Code while signed in with the same Claude account.
3. **Need help?** Ask the agent to check which connector your setup supports and install or configure it when authorized. This includes Codex CLI setups that need an MCP server. Sign in directly with the provider and review the access it requests. The agent verifies the connection with a read-only search of your application mailbox. See the [email setup guide](references/email-setup.md) for commands and troubleshooting.

```text
Help me connect my job-search email. Use the built-in connector if available.
Once I finish signing in, verify it by searching for recent application replies.
```

Web research and applications through employer forms can continue while you connect email. The skill can also use optional tools such as [Agent Reach](https://github.com/Panniantong/agent-reach) and a browser supported by your agent.

### Check application replies

Ask the skill to check your connected inbox and match replies to your tracker:

```text
$easy-apply-ai Check for replies to my applications, summarize deadlines and next steps, and update my tracker. Draft any answer that needs a new fact or commitment; don't send it without asking me.
```

The skill checks the full email thread, distinguishes acknowledgments from decisions, and flags interviews, assessments, screening questions, rejections, offers, and delivery failures. It highlights deadlines and time zones, keeps assessment credentials out of trackers, and leaves proctored interviews and tests for you to complete. It does not treat an acknowledgment as an interview or send follow-ups just because time has passed.

## How it works

```text
Your profile & goals
        ↓
Research and check the role
        ↓
Tailor with evidence from your experience
        ↓
Apply using authorized, available tools
        ↓
Record the outcome and follow up
```

For sustained searches, you can set a target and, if your agent host supports persistent goals, explicitly ask it to use one. A goal is not a guarantee of a recurring schedule or uninterrupted execution. The skill can also delegate a bounded search lane when your host supports subagents and another priority task is active.

## Privacy and control

- Keep your résumé, candidate profile, application tracker, credentials, and private messages **outside public repositories**. The included templates contain placeholders only.
- You decide which applications and messages the agent is authorized to send. The skill asks for genuinely missing facts and does not invent answers.
- Verification challenges, account access, employment assessments, and agreements must be handled according to the host's rules and the site's requirements.
- A confirmation page or sent message is evidence of an action; it is not a job offer or proof that a recruiter reviewed your application. Failed and uncertain submissions are recorded separately.

## Project structure

```text
easy-apply-ai/
├── SKILL.md                    # Main agent instructions
├── agents/openai.yaml          # Codex skill metadata
├── assets/                     # Banner and private-state templates
├── references/                 # Application, tools, and setup guidance
└── scripts/preflight.py        # Read-only tracker summary
```

To summarize a tracker without changing it:

```bash
python ~/.codex/skills/easy-apply-ai/scripts/preflight.py /path/to/applications.csv
```

Read the [application workflow](references/application-workflow.md), [delegation and tools](references/delegation-and-tools.md), and [setup and hooks](references/setup-and-hooks.md) for details.

---

<div align="center">
  Built for a more intentional job search — one opportunity at a time.
</div>
