from fastapi import Fastapi
app = Fastapi()

@app.get("/")
def read_root():
    return {"Hello": "This is version v2 of the API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


@app.get("/new-endpoint")
def new_endpoint():
    return {"message": "This is a new endpoint in version v2 of the API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)