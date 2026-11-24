<div align="center">

<img src="assets/calm-banner.png" alt="Easy Apply AI — AI-assisted job search" width="680" />

**A job search, guided by you and powered by your AI agent.**

Find relevant roles · Tailor honest applications · Keep track of what happens

[Get started](#get-started) · [How it works](#how-it-works) · [Privacy](#privacy-and-control) · [Project structure](#project-structure)

</div>

---

Searching for a job takes more than clicking Apply. You need to find roles that fit, explain your experience clearly, follow different application routes, and remember where you left off. **Easy Apply AI** is a reusable agent skill that gives your assistant a practical workflow for that process.

Tell it what you want, share your résumé and preferences, and let it help you research opportunities, prepare tailored applications, submit within your authorization, and maintain a private tracker. It can resume from information you've already provided instead of starting intake from scratch.

## What it does

| | |
| --- | --- |
| **Learns your preferences** | Uses your résumé, experience, locations, compensation, notice period, and role interests to build a candidate profile. |
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

### 2. Share your preferences

Provide your résumé or its path, target roles, preferred locations or remote arrangements, compensation expectations, notice period, and any application preferences. If you've already shared these in the session or a private profile, the skill should use that context and ask only for missing information needed to move forward.

For example:

```text
$easy-apply-ai I'm looking for remote junior AI implementation roles.
My résumé is at /path/to/resume.pdf. Target 20 applications today.
Use my existing profile and tracker, and ask if a required answer is missing.
```

### 3. Connect the tools your host supports

The skill can use an available web-research tool such as [Agent Reach](https://github.com/Panniantong/agent-reach), connected email, and a browser for application forms. Availability, account access, verification steps, and permissions depend on your environment. Installing the skill **does not** install those tools, create a scheduler, or send applications by itself.

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
