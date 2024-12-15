import random
import uuid
from datetime import datetime

def generate_mock_data():
    robots = []
    for _ in range(10):
        robots.append({
            "id": str(uuid.uuid4()),
            "status": random.choice(["online", "offline"]),
            "battery": random.randint(0, 100),
            "cpu_usage": random.randint(0, 100),
            "ram_usage": random.randint(0, 100),
            "last_updated": datetime.utcnow().isoformat(),
            "location": [round(random.uniform(-180, 180), 6), round(random.uniform(-90, 90), 6)],
        })
    return robots
