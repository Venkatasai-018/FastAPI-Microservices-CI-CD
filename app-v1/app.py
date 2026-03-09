from fastapi import Fastapi
app = Fastapi()

@app.get("/")
def read_root():
    return {"Hello": "This is version v1 of the API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

