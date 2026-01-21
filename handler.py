import uvicorn, json
from fastapi import FastAPI
from pydantic import BaseModel
from holder import Holder

# BASE CONFIG

source = "C:\\Users\\omni\\Desktop\\qa.txt"

# BASE CLASSES

store = Holder(source)
app = FastAPI()

# INPUTS

class InputDataAsk(BaseModel):
    question: str
#

class InputDataUpdate(BaseModel):
    question: str
    answer: str
#

# ENDPOINTS

# ask endpoint

@app.post("/ask")
async def ask(data: InputDataAsk):
	
    return await store.query(data.question)
#

# update QA endpoint

@app.post("/update")
async def update(data: InputDataUpdate):
    
    await store.update(data.question, data.answer)
    
    return {"status": True}
#

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )
#