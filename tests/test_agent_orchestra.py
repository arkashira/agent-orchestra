from agent_orchestra import AgentOrchestra, Agent

def test_add_agent():
    orchestra = AgentOrchestra()
    agent = Agent('test_agent', 'running')
    orchestra.add_agent(agent)
    assert len(orchestra.get_all_agents()) == 1

def test_remove_agent():
    orchestra = AgentOrchestra()
    agent = Agent('test_agent', 'running')
    orchestra.add_agent(agent)
    orchestra.remove_agent('test_agent')
    assert len(orchestra.get_all_agents()) == 0

def test_get_agent_status():
    orchestra = AgentOrchestra()
    agent = Agent('test_agent', 'running')
    orchestra.add_agent(agent)
    assert orchestra.get_agent_status('test_agent') == 'running'

def test_update_agent_status():
    orchestra = AgentOrchestra()
    agent = Agent('test_agent', 'running')
    orchestra.add_agent(agent)
    orchestra.update_agent_status('test_agent', 'stopped')
    assert orchestra.get_agent_status('test_agent') == 'stopped'

def test_get_all_agents():
    orchestra = AgentOrchestra()
    agent1 = Agent('test_agent1', 'running')
    agent2 = Agent('test_agent2', 'stopped')
    orchestra.add_agent(agent1)
    orchestra.add_agent(agent2)
    assert len(orchestra.get_all_agents()) == 2
