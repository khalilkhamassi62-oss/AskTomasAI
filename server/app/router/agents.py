from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()

class AgentBase(BaseModel):
    name: str = Field(..., example="Tomas")
    description: str | None = Field(None, example="Core orchestrator")
    version: str | None = Field(None, example="1.0")

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int

# In‑memory store
agents_db: List[Agent] = []
next_agent_id = 1

@router.get("/", response_model=List[Agent])
def list_agents():
    return agents_db

@router.post("/", response_model=Agent, status_code=status.HTTP_201_CREATED)
def create_agent(agent: AgentCreate):
    global next_agent_id
    new_agent = Agent(id=next_agent_id, **agent.dict())
    next_agent_id += 1
    agents_db.append(new_agent)
    return new_agent

@router.get("/{agent_id}", response_model=Agent)
def get_agent(agent_id: int):
    for a in agents_db:
        if a.id == agent_id:
            return a
    raise HTTPException(status_code=404, detail="Agent not found")

@router.put("/{agent_id}", response_model=Agent)
def update_agent(agent_id: int, agent: AgentCreate):
    for idx, a in enumerate(agents_db):
        if a.id == agent_id:
            updated = Agent(id=agent_id, **agent.dict())
            agents_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Agent not found")

@router.delete("/{agent_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agent(agent_id: int):
    for idx, a in enumerate(agents_db):
        if a.id == agent_id:
            del agents_db[idx]
            return
    raise HTTPException(status_code=404, detail="Agent not found")
