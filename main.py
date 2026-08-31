from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Smart LiDAR Backend Running"
    }

@app.get("/sensor")
def sensor_data():

    front = round(random.uniform(7, 25), 1)
    left = round(random.uniform(10, 25), 1)
    right = round(random.uniform(15, 30), 1)
    rear = round(random.uniform(12, 25), 1)

    nearest = min(front, left, right, rear)

    if nearest < 8:
        alert = "DANGER"
    elif nearest < 15:
        alert = "WARNING"
    else:
        alert = "SAFE"

    return {
        "sensor": "LiDAR",
        "status": "online",
        "front": front,
        "left": left,
        "right": right,
        "rear": rear,
        "nearest_obstacle": nearest,
        "alert": alert,
        "timestamp": time.strftime("%H:%M:%S")
    }