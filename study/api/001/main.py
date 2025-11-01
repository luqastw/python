from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def init():
    return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {
        "name": "first test.",
        "version": "1.0"
    }