from fastapi import APIRouter
from fastapi import HTTPException

from ..services import items

items_router = APIRouter()

prefix = ""

@items_router.get(prefix)
def find_all():
    data  = items.find_all()
    
    if not data:
        raise HTTPException(status_code=400, detail="Error")
    
    return {
        "status": 200,
        "data": data
    }

@items_router.get(prefix+"/{id}")
def find_one(id: int):
    data = items.find_one(id)
    
    if not data:
        raise HTTPException(status_code=400, detail="Error")
    
    return {
        "status": 200,
        "data": data
    }
