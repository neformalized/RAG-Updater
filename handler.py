import uvicorn
from fastapi import FastAPI

app = FastAPI()

#

@app.post("/ask")
async def ask(item: str):
	
    return {
        "status": "ok",
        "response": "ok"
    }
#

#

@app.post("/put")
async def put("/put"):
    
    return {
        "status": "ok",
        "response": "ok"
    }
#

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
#