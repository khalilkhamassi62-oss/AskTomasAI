"""CTO agent stub – mirrors Tomas stub behavior."""

from __future__ import annotations

from typing import Dict, Any


class SimpleGraph:
    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        messages = list(state.get("messages", []))
        agent_name = state.get("agent_name", "Agent")
        messages.append(f"Hello, I am {agent_name}!")
        new_state = dict(state)
        new_state["messages"] = messages
        return new_state

compiled = SimpleGraph()
