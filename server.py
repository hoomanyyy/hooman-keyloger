from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/api/getData")
def getData(data: dict):
    return {"status": "saved"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4444)