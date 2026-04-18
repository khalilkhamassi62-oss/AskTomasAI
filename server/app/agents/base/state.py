from pydantic import BaseModel
from typing import List

class AgentState(BaseModel):
    """Base state model for LangGraph agents.

    Attributes:
        agent_name: Name of the agent (e.g., "Tomas").
        messages: List of message strings exchanged during the conversation.
    """

    agent_name: str
    messages: List[str] = []
