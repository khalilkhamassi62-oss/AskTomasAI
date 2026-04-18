from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel

from ..dependencies import create_access_token, decode_token, TokenData

router = APIRouter()

# For demo purposes we accept any username/password and return a token
# In a real system you would verify hashed passwords against a DB.
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Stub user validation – accept any credentials
    if not form_data.username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username required")
    access_token = create_access_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        token_data = decode_token(token)
        return token_data
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

@router.get("/me")
async def read_current_user(current_user: TokenData = Depends(get_current_user)):
    return {"username": current_user.username}
