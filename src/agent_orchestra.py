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

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def remove_agent(self, agent_name: str):
        self.agents = [agent for agent in self.agents if agent.name != agent_name]

    def get_agent_status(self, agent_name: str):
        for agent in self.agents:
            if agent.name == agent_name:
                return agent.status
        return None

    def update_agent_status(self, agent_name: str, status: str):
        for agent in self.agents:
            if agent.name == agent_name:
                agent.status = status
                return

    def get_all_agents(self):
        return self.agents

def main():
    parser = argparse.ArgumentParser(description='Agent Orchestra')
    parser.add_argument('--add', help='Add an agent')
    parser.add_argument('--remove', help='Remove an agent')
    parser.add_argument('--status', help='Get an agent status')
    parser.add_argument('--update', help='Update an agent status')
    parser.add_argument('--list', action='store_true', help='List all agents')
    args = parser.parse_args()

    orchestra = AgentOrchestra()

    if args.add:
        agent_name, agent_status = args.add.split(',')
        orchestra.add_agent(Agent(agent_name, agent_status))
    elif args.remove:
        orchestra.remove_agent(args.remove)
    elif args.status:
        print(orchestra.get_agent_status(args.status))
    elif args.update:
        agent_name, agent_status = args.update.split(',')
        orchestra.update_agent_status(agent_name, agent_status)
    elif args.list:
        for agent in orchestra.get_all_agents():
            print(f'{agent.name}: {agent.status}')

if __name__ == '__main__':
    main()
