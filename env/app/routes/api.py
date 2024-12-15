from fastapi import APIRouter
from app.mock_data import generate_mock_data

router = APIRouter()

robots = generate_mock_data()

@router.get("/robots")
def get_robots():
    return {"robots": robots}
