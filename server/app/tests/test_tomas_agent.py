import pytest

from server.app.agents.tomas.stategraph import compiled
from server.app.agents.base.state import AgentState

def test_tomas_greeting():
    # Initialize state with empty messages
    init_state = AgentState(agent_name="Tomas", messages=[])
    # Invoke the compiled graph
    result = compiled.invoke(init_state.dict())
    # Expect the result to contain a greeting message
    messages = result.get("messages", [])
    assert any("Hello" in msg for msg in messages), "Greeting not found in messages"
