from fastapi import FastAPI
from time import sleep
import asyncio

app = FastAPI()


@app.get("/fastapi")
async def read_root():
    await asyncio.sleep(0.200)
    return {"Hello": "FastAPI"}
