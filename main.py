from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from crag import generateResponse
import uvicorn
app = FastAPI()


class QueryRequest(BaseModel):
    query: str = Field(..., max_length=200)

@app.get("/")
def root():
    return {"message": "Welcome to the SteamMind API"}

@app.post("/get_response")
async def get_response(request: QueryRequest):
    try:
        user_input = request.query.lower()
        bot_response = generateResponse(user_input)
        
        return {"response": bot_response}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)