from fastapi import FastAPI, Body

app = FastAPI()
items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_items(item: str = Body()):
    items.append(item)
    return items
