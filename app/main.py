from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from pydantic import BaseModel
from os import environ
import redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_HOST = environ.get('REDIS_HOST', '127.0.0.1')
rd = redis.Redis(host=REDIS_HOST, port=6379, db=0)

class Item(BaseModel):
    key: str
    value: str

@app.get("/")
def read_root():
    return JSONResponse(content={"success": True, "message": "Hello World!"})

@app.post("api/v1/store", summary="Store new data (key/value)")
def store(item: Item):
    exist = rd.get(item.key)

    if exist is not None:
        return JSONResponse(content={"success": False, "message": "Item has already been saved!"}, status_code=status.HTTP_409_CONFLICT) 
    else:
        rd.set(item.key, item.value)
        return JSONResponse(content={"success": True, "message": "Item successfully stored!"})

@app.get("api/v1/show/{key}", summary="Show stored data (key/value)")
def show(key):
    result = rd.get(key)

    if result is not None:
        decoded_result = result.decode('utf-8')
        return JSONResponse(content={"success": True, "result": decoded_result})
    else:
        return JSONResponse(content={"success": False, "message": "Selected item not found!"}, status_code=status.HTTP_404_NOT_FOUND)

