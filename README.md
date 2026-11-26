<div align="center">

<img src="assets/calm-banner.png" alt="Easy Apply AI â AI-assisted job search" width="680" />

**A job search, guided by you and powered by your AI agent.**

Find relevant roles Â· Tailor honest applications Â· Keep track of what happens

[Get started](#get-started) Â· [How it works](#how-it-works) Â· [Privacy](#privacy-and-control) Â· [Project structure](#project-structure)

</div>

---

Searching for a job takes more than clicking Apply. You need to find roles that fit, explain your experience clearly, follow different application routes, and remember where you left off. **Easy Apply AI** is a reusable agent skill that gives your assistant a practical workflow for that process.

Tell it what you want, share your rÃ©sumÃ© and preferences, and let it help you research opportunities, prepare tailored applications, submit within your authorization, and maintain a private tracker. It can resume from information you've already provided instead of starting intake from scratch.

## What it does

| | |
| --- | --- |
| **Learns your preferences** | Uses your rÃ©sumÃ©, experience, locations, compensation, notice period, and role interests to build a candidate profile. |
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
$easy-apply-ai Help me find and apply for jobs that fit my experience.
```

For other agent hosts, install this folder according to their Agent Skills instructions. The skill's instructions are in [SKILL.md](SKILL.md).

### 2. Start with what you want to do

Tell the agent what kind of work you want and why: the problems you want to solve, role families or causes you want to explore, preferred work setup, and work you want to avoid. Then share your rÃ©sumÃ© or its path, plus practical constraints such as location, compensation, and notice period. The agent uses your rÃ©sumÃ© to verify skills and experience and to tailor applications; it should not guess your interests from rÃ©sumÃ© keywords or let your past job titles decide your next move.

For example:

```text
$easy-apply-ai I want to explore remote junior AI consulting and AI-native engineering roles, including mission-driven organizations. I want to avoid senior and teaching jobs.
My rÃ©sumÃ© is at /path/to/resume.pdf. Target 20 applications today.
Use my existing profile and tracker, and ask if a required answer is missing.
```

The skill should search from those stated interests, then connect suitable openings to evidence in the rÃ©sumÃ© and projects. A rÃ©sumÃ© helps show what the person can do; the person sets the direction.

### 3. Connect the tools your host supports

The skill can use an available web-research tool such as [Agent Reach](https://github.com/Panniantong/agent-reach), connected email, and a browser for application forms. Availability, account access, verification steps, and permissions depend on your environment. Installing the skill **does not** install those tools, create a scheduler, or send applications by itself.

For email, first use the connector your agent host already supports. In ChatGPT/Codex, open the Plugins directory, choose Gmail or Outlook Email, install it if needed, select **Connect**, sign in to the account you want to search, and review the requested permissions. In Claude Code, connect Gmail or another mail provider under [Claude connectors](https://claude.ai/customize/connectors), complete provider authorization, then run `/mcp` to see the available connector in your CLI session. If your host has no built-in connector, ask the skill to find a trusted MCP option and explain its source and requested access before setup. You sign in directly with the provider; never paste passwords, tokens, or verification codes into chat. See [email connection and setup](references/email-setup.md) for host-specific details and troubleshooting.

### Check application replies

Ask the skill to check your connected inbox and match replies to your tracker:

```text
$easy-apply-ai Check for replies to my applications, summarize deadlines and next steps, and update my tracker. Draft any answer that needs a new fact or commitment; don't send it without asking me.
```

The skill checks the full email thread, distinguishes acknowledgments from decisions, and flags interviews, assessments, screening questions, rejections, offers, and delivery failures. It highlights deadlines and time zones, keeps assessment credentials out of trackers, and leaves proctored interviews and tests for you to complete. It does not treat an acknowledgment as an interview or send follow-ups just because time has passed.

## How it works

```text
Your profile & goals
        â
Research and check the role
        â
Tailor with evidence from your experience
        â
Apply using authorized, available tools
        â
Record the outcome and follow up
```

For sustained searches, you can set a target and, if your agent host supports persistent goals, explicitly ask it to use one. A goal is not a guarantee of a recurring schedule or uninterrupted execution. The skill can also delegate a bounded search lane when your host supports subagents and another priority task is active.

## Privacy and control

- Keep your rÃ©sumÃ©, candidate profile, application tracker, credentials, and private messages **outside public repositories**. The included templates contain placeholders only.
- You decide which applications and messages the agent is authorized to send. The skill asks for genuinely missing facts and does not invent answers.
- Verification challenges, account access, employment assessments, and agreements must be handled according to the host's rules and the site's requirements.
- A confirmation page or sent message is evidence of an action; it is not a job offer or proof that a recruiter reviewed your application. Failed and uncertain submissions are recorded separately.

## Project structure

```text
easy-apply-ai/
âââ SKILL.md                    # Main agent instructions
âââ agents/openai.yaml          # Codex skill metadata
âââ assets/                     # Banner and private-state templates
âââ references/                 # Application, tools, and setup guidance
âââ scripts/preflight.py        # Read-only tracker summary
```

To summarize a tracker without changing it:

```bash
python ~/.codex/skills/easy-apply-ai/scripts/preflight.py /path/to/applications.csv
```

Read the [application workflow](references/application-workflow.md), [delegation and tools](references/delegation-and-tools.md), and [setup and hooks](references/setup-and-hooks.md) for details.

---

<div align="center">
  Built for a more intentional job search â one opportunity at a time.
</div>
