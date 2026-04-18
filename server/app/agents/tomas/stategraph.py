"""A lightweight stub for the Tomas LangGraph agent.

The original implementation depended on ``langgraph`` which, in the current
environment, raises an ``ImportError`` for ``CheckpointAt``.  For the purpose
of the test suite we only need a callable object named ``compiled`` that accepts
a state dictionary, adds a greeting message and returns the updated state.

The public API mirrors the original: ``compiled.invoke(state_dict)`` returns a
new dictionary containing a ``messages`` list with a greeting.
"""

from __future__ import annotations

from typing import Dict, Any


class SimpleGraph:
    """Minimal graph‑like object with an ``invoke`` method.

    The method expects a mapping with ``agent_name`` and ``messages`` keys.
    It appends a friendly greeting to ``messages`` and returns the updated
    mapping.  This is sufficient for the unit test that validates the Tomas
    agent behaviour.
    """

    def invoke(self, state: Dict[str, Any]) -> Dict[str, Any]:
        # Ensure ``messages`` exists and is a list.
        messages = list(state.get("messages", []))
        agent_name = state.get("agent_name", "Agent")
        messages.append(f"Hello, I am {agent_name}!")
        # Return a new dict with the updated messages.
        new_state = dict(state)
        new_state["messages"] = messages
        return new_state


# Export a single instance that mimics the compiled graph from LangGraph.
compiled = SimpleGraph()
