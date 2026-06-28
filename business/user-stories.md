Generated `/tmp/user-stories.md` for **agent-orchestra** — 12 stories across 4 epics, Connextra format, each with 4 acceptance criteria + S/M/L complexity.

**Epics & stories:**
1. **Spin Up & Run Agents** — fleet launch (`orchestra up`), BYO agent binary, per-agent worktree isolation
2. **Observe & Interact** — unified TUI dashboard, attach-to-blocked-agent, aggregated filterable logs
3. **Coordinate Work** — declarative task assignment, `depends_on` ordering, shared scratch context
4. **Control & Sustainability** — graceful teardown, local-first/no-quota, resource guardrails

**Key strategic calls baked in:**
- **MVP cut** = launch → observe → attach → teardown (proves the hypothesis before any coordination logic).
- **Defensible sliver** = interactive attach + dependency ordering — the gap `tmux`/process managers leave open.
- **Scope guardrail** flagged for PRD: keep coordination lightweight (config + `depends_on`), *not* a LangGraph-class DAG engine — adopting one would reproduce the exact "overengineering" the validated pain rejects.

Note: the file previously held a stale `pain-sentry` deliverable from an earlier pipeline run; I overwrote it with this product's stories.