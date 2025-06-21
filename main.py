# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
servers = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register(request: Request):
    data = await request.json()
    if data not in servers:
        servers.append(data)
    return {"status": "registered"}

@app.get("/servers")
def get_servers():
    return servers
