import argparse
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    name: str
    status: str

class AgentOrchestra:
    def __init__(self):
        self.agents = []

    def add_agent(self, name: str):
        self.agents.append(Agent(name, "idle"))

    def remove_agent(self, name: str):
        self.agents = [agent for agent in self.agents if agent.name != name]

    def update_agent_status(self, name: str, status: str):
        for agent in self.agents:
            if agent.name == name:
                agent.status = status
                break

    def get_agent_status(self, name: str):
        for agent in self.agents:
            if agent.name == name:
                return agent.status
        return None

    def list_agents(self):
        return [agent.name for agent in self.agents]

def main():
    parser = argparse.ArgumentParser(description="Agent Orchestra")
    parser.add_argument("--add", help="Add an agent")
    parser.add_argument("--remove", help="Remove an agent")
    parser.add_argument("--update", help="Update an agent's status")
    parser.add_argument("--status", help="Get an agent's status")
    parser.add_argument("--list", action="store_true", help="List all agents")
    args = parser.parse_args()

    orchestra = AgentOrchestra()

    if args.add:
        orchestra.add_agent(args.add)
    elif args.remove:
        orchestra.remove_agent(args.remove)
    elif args.update:
        name, status = args.update.split(",")
        orchestra.update_agent_status(name, status)
    elif args.status:
        print(orchestra.get_agent_status(args.status))
    elif args.list:
        print(json.dumps(orchestra.list_agents()))

if __name__ == "__main__":
    main()
