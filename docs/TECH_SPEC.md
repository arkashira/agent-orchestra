# TECH_SPEC.md

## Technical Specification for Agent Orchestra

### 1. Introduction
Agent Orchestra is a centralized orchestration system designed to manage the lifecycle of coding agents within Axentx's autonomous AI workforce pipeline. It coordinates task assignment, monitors agent performance, and ensures efficient execution of software development workflows (e.g., requirement specification, design, development, testing). The system integrates with the company's shared BRAIN (pgvector) to leverage vector-based skill matching and knowledge retrieval.

### 2. Architecture Overview
Agent Orchestra follows a microservices architecture with four core components:
- **Agent Manager Service**: Orchestrates agent lifecycle (creation, assignment, termination).
- **Task Queue Service**: Prioritizes and routes tasks to available agents based on skill and workload.
- **Monitoring Dashboard Service**: Provides real-time metrics
