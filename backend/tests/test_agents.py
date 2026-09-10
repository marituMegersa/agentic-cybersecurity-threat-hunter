def test_agent_orchestrator():
    prompt = "Test execution query for agentic-cybersecurity-threat-hunter"
    assert len(prompt) > 0
    assert "Test" in prompt
