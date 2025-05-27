from fastapi import FastAPI, Request

app = FastAPI()

memory = {}

@app.post("/write")
async def write_memory(data: dict):
    user_id = data.get("user_id")
    text = data.get("text")
    if not user_id or not text:
        return {"error": "Missing user_id or text"}
    
    memory.setdefault(user_id, []).append(text)
    return {"status": "ok", "message": f"Saved for {user_id}"}

@app.post("/read")
async def read_memory(data: dict):
    user_id = data.get("user_id")
    if not user_id:
        return {"error": "Missing user_id"}
    
    return {"memory": memory.get(user_id, [])}
