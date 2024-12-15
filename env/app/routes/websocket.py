from fastapi import APIRouter, WebSocket
from app.mock_data import generate_mock_data

router = APIRouter()
robots = generate_mock_data()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Simulate updates
        for robot in robots:
            robot["battery"] = max(0, robot["battery"] - 1)  # Decrease battery
        await websocket.send_json({"robots": robots})
