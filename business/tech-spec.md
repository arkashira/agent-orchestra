Generated `/tmp/tech-spec.md` — v1 technical spec for **agent-orchestra** (overwrote a stale `pain-sentry` spec that was sitting at that path).

Spec is built around the hypothesis's core constraint — *anti-overengineering, local-first, no billing limits* — and makes that opinionated throughout:

- **Stack** — TS/Node 20 + Ink TUI + `node-pty` (real PTYs so each agent's own TUI renders), with a ~700-LOC in-process supervisor instead of LangGraph/Temporal/Redis. Explicitly named non-goals (no K8s, no broker, no Docker requirement).
- **Hosting** — local CLI = nothing to host; supporting infra (npm, GH Releases, Cloudflare Workers) lands at **~$0/mo**.
- **Data model** — 6 SQLite tables (agents, runs, tasks w/ a `depends_on` DAG, messages, worktrees, events) with indexes; replayable.
- **API** — 10 endpoints on an opt-in loopback `--serve` server, including `/stdin` for interactive steering and `/merge` for worktree merge-back, plus a WS live stream.
- **Security** — loopback-default + bearer-token-when-exposed, secrets never on disk + redacted in logs, git-worktree blast-radius isolation, Sigstore-signed binaries.
- **Observability** — pino JSON logs, per-run parallelism-factor metric, opt-in OTel (off by default), and a `replay` command.
- **Build/CI** — pnpm + biome + vitest with a PTY integration test, gitleaks/npm-audit gates, signed multi-platform Bun binaries.

The strongest opinion baked in: the orchestration core is deliberately *not* a durable-execution engine — that's the differentiator vs. heavier multi-agent frameworks the audience is reacting against.