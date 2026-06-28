```markdown
# Customer Journey Map – agent‑orchestra

| Phase | Trigger Event | Friction Points | User Emotions | Opportunities to Delight | Key Metric |
|-------|----------------|-----------------|---------------|--------------------------|------------|
| **Aware** | • Reading a blog post or watching a short demo on “how to run multiple local coding agents”<br>• Seeing a tweet from a peer who solved a complex refactor with agent‑orchestra | • Limited visibility of the tool in search results<br>• Confusion between “agent orchestration” and “workflow automation” | Curious, slightly overwhelmed | • SEO‑optimized landing page with a 30‑second explainer video<br>• Social proof badge (e.g., “Used by 1,200+ devs”) | % of website visitors who view the product page |
| **Consider** | • Downloading the repo or cloning the starter kit<br>• Attending a live webinar that walks through a real‑world use case | • Lack of clear installation steps for different OS<br>• Fear of breaking existing local environment | Skeptical, hopeful | • One‑click “Install on macOS/Linux/Windows” scripts<br>• Interactive CLI wizard that auto‑detects existing tools (Git, Docker, VS Code) | % of visitors who download the repo or clone the repo |
| **Try** | • Running the first orchestration script (`agent-orchestra run`)<br>• Encountering a “missing dependency” error | • Dependency resolution failures<br>• Unclear error messages<br>• No visual feedback on agent status | Frustrated, determined | • Real‑time terminal UI showing agent states (running, idle, error)<br>• Auto‑repair suggestions (e.g., “Install missing libXYZ”) | Time to first successful orchestration run |
| **Adopt** | • Completing a multi‑step coding task (e.g., auto‑generate tests, refactor, lint) with agent‑orchestra<br>• Sharing results on Slack or GitHub | • Limited documentation on advanced features (e.g., custom agent plugins)<br>• Integration gaps with existing CI/CD pipelines | Confident, proud | • One‑click “Export to GitHub Actions” template<br>• In‑app “Show me how to add a new agent” guided tour | % of users who add at least one custom agent |
| **Expand** | • Scaling to 5+ agents for a large monorepo<br>• Requesting new features (e.g., agent‑to‑agent communication, persistence) | • Performance bottlenecks with many agents<br>• Lack of monitoring & logging for production use | Empowered, visionary | • Built‑in metrics dashboard (CPU, memory per agent)<br>• Plugin marketplace for community‑built agents | Net Promoter Score (NPS) & number of community‑submitted agents |

> **Notes for the product team**  
> - **Trigger events** are the moments that push a user from one phase to the next; they should be surfaced prominently in marketing and onboarding.  
> - **Friction points** are the pain‑points that can be turned into delightful moments if addressed.  
> - **User emotions** help prioritize which friction points to tackle first (e.g., frustration in the Try phase is a high‑impact area).  
> - **Opportunities to delight** are quick wins that can turn a neutral or negative experience into a positive one.  
> - **Key metrics** should be tracked in the product analytics stack to validate the hypothesis that agent‑orchestra solves the identified pain.  

```