from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()

class CompanyBase(BaseModel):
    name: str = Field(..., example="Acme Corp")
    domain: str | None = Field(None, example="acme.com")

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

# In‑memory store – replace with DB calls in production
companies_db: List[Company] = []
next_id = 1

@router.get("/", response_model=List[Company])
def list_companies():
    return companies_db

@router.post("/", response_model=Company, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate):
    global next_id
    new_company = Company(id=next_id, **company.dict())
    next_id += 1
    companies_db.append(new_company)
    return new_company

@router.get("/{company_id}", response_model=Company)
def get_company(company_id: int):
    for comp in companies_db:
        if comp.id == company_id:
            return comp
    raise HTTPException(status_code=404, detail="Company not found")

@router.put("/{company_id}", response_model=Company)
def update_company(company_id: int, company: CompanyCreate):
    for idx, comp in enumerate(companies_db):
        if comp.id == company_id:
            updated = Company(id=company_id, **company.dict())
            companies_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Company not found")

@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: int):
    for idx, comp in enumerate(companies_db):
        if comp.id == company_id:
            del companies_db[idx]
            return
    raise HTTPException(status_code=404, detail="Company not found")
