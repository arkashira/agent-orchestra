```markdown
# dataflow.md

## System Dataflow Architecture – agent‑orchestra

```
┌───────────────────────┐
│  External Data Sources │
│  (Git repos, IDE APIs, │
│   local file system)   │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   Ingestion Layer      │
│   (CLI adapters,       │
│    file‑watchers,      │
│    webhook listeners) │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ Processing/Transform   │
│   Layer                │
│   • Agent‑state        │
│   • Task‑queue         │
│   • Dependency graph   │
│   • Security sandbox   │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   Storage Tier         │
│   • SQLite (local)     │
│   • Redis (in‑memory)  │
│   • Optional S3 backup │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ Query/Serving Layer    │
│   • REST/CLI API       │
│   • WebSocket hub      │
│   • Auth: JWT + RBAC  │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│ Egress to User         │
│   • Terminal UI        │
│   • VSCode Extension   │
│   • Web Dashboard      │
└───────────────────────┘
```

### Component Breakdown by Tier

| Tier | Component | Purpose | Auth Boundary |
|------|-----------|---------|---------------|
| **External Data Sources** | GitHub / GitLab repos | Source code for agents to analyze | None (public repos) |
| | IDE APIs (VSCode, JetBrains) | Capture editor events | None (local) |
| | File system watcher | Detect new/changed files | None (local) |
| **Ingestion Layer** | CLI adapters | Accept commands like `agent-orchestra run` | User‑level CLI auth (token) |
| | File‑watcher daemon | Push file events to ingestion queue | Local process auth |
| | Webhook listener | Receive external triggers (e.g., CI hooks) | HMAC signature verification |
| **Processing/Transform Layer** | Agent‑state manager | Keeps per‑agent context & history | Internal, no external exposure |
| | Task‑queue orchestrator | Schedules agent tasks, respects dependencies | Internal |
| | Dependency graph builder | Resolves agent inter‑dependencies | Internal |
| | Security sandbox | Runs agents in isolated containers | Container runtime auth |
| **Storage Tier** | SQLite DB | Persist agent configs, logs, state | Local file encryption |
| | Redis cache | Fast in‑memory task status | Local process auth |
| | S3 backup (optional) | Durable persistence for long‑running jobs | IAM role with limited scope |
| **Query/Serving Layer** | REST/CLI API | Expose orchestration commands | JWT + role‑based access |
| | WebSocket hub | Real‑time status updates to UI | JWT + origin check |
| | Auth service | Issue/validate JWT, manage roles | Internal |
| **Egress to User** | Terminal UI (CLI) | Interactive command line interface | Uses CLI auth token |
| | VSCode Extension | Inline agent output, status panel | Extension auth via OAuth |
| | Web Dashboard | Graphical overview, logs | JWT + RBAC |

### Auth & Security Highlights

- **JWT** issued by the local auth service for CLI and web clients; signed with a short‑lived key.
- **Role‑Based Access Control (RBAC)**: `admin`, `developer`, `viewer` roles; only `admin` can modify agent configs.
- **Containerized Agent Execution**: each agent runs in a lightweight Docker container with `--cap-drop ALL` and `--read-only` filesystem.
- **HMAC Verification** for incoming webhooks to prevent spoofing.
- **Local File Encryption** for SQLite database using `libsodium` to protect sensitive logs.

This architecture keeps the orchestration lightweight, fully local, and secure while providing extensibility for future integrations (e.g., cloud‑based storage, external CI/CD pipelines).