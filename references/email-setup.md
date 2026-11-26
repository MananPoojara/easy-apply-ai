# Email access and setup

Use this guide during job-search setup when the user wants email applications or reply tracking, or whenever a mailbox connection is missing or fails. Check which host, provider, and mailbox the user wants to use. Reuse a working connection and check which actions it supports, since some connectors can search or draft but cannot send or attach files.

## Codex desktop or ChatGPT

1. Open **Plugins** or **Settings → Plugins**. Search for **Gmail** or **Outlook Email**.
2. Install the plugin if prompted, then select **Connect**. If the host provides a setup action and the user has authorized setup, use it and hand off at sign-in.
3. Have the user sign in to the provider account they use for applications and review the requested access in the provider's authorization screen.
4. In a Codex task view with **Sources → Use plugins**, select the installed plugin. If it does not appear, check the surface and workspace settings. A workspace administrator may need to enable the plugin or approve the account domain.

[OpenAI plugin guide](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Connecting app accounts](https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt)

## Claude Code

1. Sign in to Claude with the account you use in Claude Code and open [Claude connectors](https://claude.ai/customize/connectors).
2. Select Gmail or Microsoft 365 if available. Complete provider authorization for the intended mailbox.
3. In Claude Code, run `/mcp` and check that the account connector is available.

Claude Code loads claude.ai connectors for supported Claude subscription logins. If you use an API key or a third-party model provider, check the MCP option below. Anthropic-hosted Gmail and Microsoft 365 connectors require authorization through claude.ai. Adding their URLs locally does not enable local OAuth.

[Claude Code account connectors](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai)

## Codex CLI or another setup without a built-in connector

Check for an existing mail MCP with `codex mcp list` or `claude mcp list`. If none fits, identify a provider-supported or trusted MCP server. Tell the user who maintains it, where mailbox data is processed, and which read, draft, send, or modify permissions it requests. Use the least access the connector supports for the work requested.

When the user authorizes setup and the host permits it, run the verified server's documented configuration commands. For a remote HTTP server that supports the host's OAuth flow, these are the command shapes. Replace `VERIFIED_SERVER_URL` with the vendor's documented MCP endpoint.

```bash
# Codex CLI
codex mcp add job-mail --url VERIFIED_SERVER_URL
codex mcp login job-mail  # if the add step didn't already complete OAuth
codex mcp list

# Claude Code, for a separately hosted MCP server
claude mcp add --transport http job-mail VERIFIED_SERVER_URL
claude mcp list
```

In Claude Code, use `/mcp` to open the server's authentication flow if prompted. In either host, let the user sign in directly through the provider. Keep local mailbox configuration and credentials out of shared repos and never ask for passwords, tokens, or one-time codes in chat. If you cannot run setup, give the user the exact next step for their host and continue work that can proceed without email.

[Codex MCP configuration](https://developers.openai.com/codex/mcp) · [Claude Code MCP installation](https://code.claude.com/docs/en/mcp#installing-mcp-servers)

## Verify before using email

- Confirm which mailbox is connected, especially when several accounts are available.
- Run a read-only search for a known recruiter, role, or recent application subject. An empty result can be valid if the search succeeded against the intended mailbox. A connector appearing in a list is only evidence that it is configured.
- If the connector lacks a needed action such as sending attachments, explain which action is unavailable and continue with supported work. Use existing authorization for external actions. Connector access alone does not authorize sending messages or changing mailbox contents.
