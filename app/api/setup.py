import random
from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/random-number")
async def get_random_number(min: int = 1, max: int = 6):
    """Return a random number between min and max."""
    random_number = random.randint(min, max)
    return {"random_number": random_number}

