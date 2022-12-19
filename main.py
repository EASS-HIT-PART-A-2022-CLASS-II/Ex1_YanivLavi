import json
from models import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello, feel free to use /docs"

@app.post("/add")
def add(track: Track):
    return {"Track was added":  add_track(track)}

@app.post("/del")
def delete(track: Track):
    return {"Track was deleted":  delete_track(track)}

@app.post("/info")
def info(id):
    return {"Track info":  track_info(id)}


# @app.post("/del")
# def delete(track: Track):
#     return {"Track was deleted":  delete_track(track)}
