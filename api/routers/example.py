from fastapi import APIRouter, Depends
from dependencies import get_db

router = APIRouter()

@router.get("/version")
def get_version(db = Depends(get_db)):
    return "0.0.1"