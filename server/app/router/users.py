from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import List

router = APIRouter()

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    role: str = Field(..., example="admin")

class UserCreate(UserBase):
    password: str = Field(..., example="secret")

class User(UserBase):
    id: int

# In‑memory store
users_db: List[User] = []
next_user_id = 1

@router.get("/", response_model=List[User])
def list_users():
    return users_db

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global next_user_id
    new_user = User(id=next_user_id, email=user.email, role=user.role)
    next_user_id += 1
    users_db.append(new_user)
    # Password would be hashed and stored elsewhere in a real system
    return new_user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in users_db:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            updated = User(id=user_id, email=user.email, role=user.role)
            users_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            del users_db[idx]
            return
    raise HTTPException(status_code=404, detail="User not found")
