import uvicorn, json
from fastapi import FastAPI
from pydantic import BaseModel
from holder import Holder

# base config

source = "C:\\Users\\omni\\Desktop\\qa.txt"

# base classes

store = Holder(source)
app = FastAPI()

# input & output classes

class InputDataAsk(BaseModel):
    question: str
#

class InputDataUpdate(BaseModel):
    question: str
    answer: str
#

# endpoints

@app.post("/ask")
async def ask(data: InputDataAsk):
	
    print(data.question)
    
    response = await store.query(data.question)
    
    print(response)
    
    return {
        "status": "ok",
        "response": response
    }
#

#

@app.post("/update")
async def update(data: InputDataUpdate):
    
    return {
        "status": "ok",
        "response": "ok"
    }
#

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )
#