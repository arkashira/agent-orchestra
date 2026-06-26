from agent_orchestra import AgentOrchestra, Agent

def test_add_agent():
    orchestra = AgentOrchestra()
    orchestra.add_agent("agent1")
    assert len(orchestra.agents) == 1
    assert orchestra.agents[0].name == "agent1"
    assert orchestra.agents[0].status == "idle"

def test_remove_agent():
    orchestra = AgentOrchestra()
    orchestra.add_agent("agent1")
    orchestra.remove_agent("agent1")
    assert len(orchestra.agents) == 0

def test_update_agent_status():
    orchestra = AgentOrchestra()
    orchestra.add_agent("agent1")
    orchestra.update_agent_status("agent1", "running")
    assert orchestra.agents[0].status == "running"

def test_get_agent_status():
    orchestra = AgentOrchestra()
    orchestra.add_agent("agent1")
    assert orchestra.get_agent_status("agent1") == "idle"
    orchestra.update_agent_status("agent1", "running")
    assert orchestra.get_agent_status("agent1") == "running"

def test_list_agents():
    orchestra = AgentOrchestra()
    orchestra.add_agent("agent1")
    orchestra.add_agent("agent2")
    assert len(orchestra.list_agents()) == 2
    assert "agent1" in orchestra.list_agents()
    assert "agent2" in orchestra.list_agents()
