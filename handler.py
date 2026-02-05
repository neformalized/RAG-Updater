import uvicorn, json
from fastapi import FastAPI
from pydantic import BaseModel
from holder import Holder

# BASE CONFIG

source = "C:\\Users\\omni\\Desktop\\temp\\qa.txt"

# BASE CLASSES

store = Holder(source)
app = FastAPI()

# INPUTS

class InputDataAsk(BaseModel):
    ask: str
#

class InputDataUpdate(BaseModel):
    ask: str
    answer: str
#

# ENDPOINTS

# ask endpoint

@app.post("/ask")
async def ask(data: InputDataAsk):
	
    return await store.query(data.ask)
#

# update QA endpoint

@app.post("/update")
async def update(data: InputDataUpdate):
    
    await store.update(data.ask, data.answer)
    
    return {"status": True}
#

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )
#