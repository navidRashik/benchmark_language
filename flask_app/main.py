from flask import Flask
from time import sleep
import asyncio

app = Flask(__name__)


@app.route("/flask")
def hello_world():
    # await asyncio.sleep(0.200)
    sleep(0.2)
    return {"Hello": "Flask"}
