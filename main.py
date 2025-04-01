
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/ok")
def read_root():
    return {"status": "ok"}


