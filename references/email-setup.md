# Email access and setup

Use this guide when the user asks for inbox checks, application-reply triage, delivery-failure checks, or application emails and no connected mailbox tool is available yet.

## Choose the host's supported connector first

Check whether the current host exposes Gmail, Outlook Email, or another mail connector and whether the intended account is connected. Do not assume that installing the skill connected an account. If a connector is present but disconnected, give the user the relevant steps below and continue independent job-search work while they connect it.

### ChatGPT or Codex

1. Open **Plugins** (or **Settings â Plugins**, depending on the surface) and find Gmail or Outlook Email.
2. Install the plugin if prompted, then select **Connect**.
3. Sign in to the provider account that contains the application mail, review the requested permissions, and finish the provider authorization.
4. In Codex, select the installed plugin in **Sources â Use plugins** when the current task needs it. Available apps, actions, plans, and workspace permissions vary.

If an app is missing or marked unavailable, check the workspace's plugin/app controls. A workspace or mail-provider administrator may need to enable or approve it. Official guides: [connect an app account](https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt) and [plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

### Claude Code

For Anthropic-hosted Gmail, Microsoft 365, or Google Calendar connectors, use the account-level connector flow rather than a local OAuth workaround:

1. Sign in to Claude with the user's own Claude account and open [Claude connectors](https://claude.ai/customize/connectors).attachments
2. Add the mail connector and complete the provider's authorization flow for the intended mailbox.
3. In Claude Code, run `/mcp` and check that the connector is listed and available.

Claude Code receives account connectors from claude.ai when the active login is a claude.ai subscription account. They are not loaded when Claude Code is authenticated with an API key or a third-party model provider. Anthropic-hosted Gmail and Microsoft 365 connectors do not support local OAuth from Claude Code; connect them through claude.ai. See [Claude Code's MCP connector guide](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai).

For a different, independently hosted mail MCP server, first verify its maintainer, source, transport, permissions, data handling, and OAuth support. Explain the server and access it requests before installing it. If installation is authorized and supported, configure it at the narrowest suitable scope, let the user complete OAuth directly, and use `/mcp` or `claude mcp list` to verify the connection. Do not put provider secrets in a project file or ask the user to paste them into chat. See [Claude Code's MCP installation and authentication guide](https://code.claude.com/docs/en/mcp).

## If no suitable connector is available

1. Explain which capability is missing and name the user's host.
2. Offer the host's official connection steps when available. If not, research a reputable MCP server from a vendor or trusted directory and present its maintainer, install source, requested scopes, and whether it can read, search, send, or modify mail.
3. Install or change local configuration only when the user has authorized that setup and the host permits it. Keep the user's provider sign-in in the official browser/OAuth flow; never handle credentials in chat.
4. If setup cannot be completed, offer the user a clear manual next step and continue other useful work.

## Verify access and keep the scope narrow

- Confirm which provider account is connected; multiple accounts can be available.
- Use a read-only search for recent application mail to verify access. Do not send a test email or modify mail just to test the connector.
- Read relevant threads and attachmments only as needed to identify the job outcome and next action.
- Connector setup does not authorize sending an email, accepting a consent, submitting an application, or changing mailbox contents. Follow the user's existing authorization and host approval rules for each external action.
