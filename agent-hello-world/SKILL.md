---
name: agent-hello-world
description: Create a minimal hello-world response, prompt, or starter example for an AI agent. Use when Codex is asked for an agent greeting, hello-world skill demonstration, smoke-test response, or tiny first-run agent example.
---

# Agent Hello World

## Quick Start

Produce the smallest useful hello-world artifact for the requested format. If no format is specified, respond with:

```text
Hello, world! I'm an agent, awake and ready to help.
```

## Workflow

1. Identify the requested output type: plain text, prompt, code snippet, or test fixture.
2. Keep the result minimal, friendly, and easy to verify.
3. Use the user's requested language, runtime, or voice if they provide one.
4. Avoid adding setup instructions, dependencies, or architecture unless the user asks for them.

## Examples

- For a plain greeting: `Hello, world! I'm your agent, ready to help.`
- For a prompt: `You are a helpful agent. Start by saying: Hello, world! I am ready to help.`
- For code: return the shortest executable snippet that prints or returns an agent hello-world message.
