from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return{"message":"welcome to fastapi"}

# About Route
@app.get("/about")
def about():
    return{"message":"this is about page"}

# Users Route
@app.get("/users")
def route():
    return{"message":"this is users route"}
