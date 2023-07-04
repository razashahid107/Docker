import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"FROM:{'ENV','DEFAULT_ENV'}"}

