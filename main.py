from fastapi import FastAPI, BackgroundTasks
from asyncio import sleep

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
