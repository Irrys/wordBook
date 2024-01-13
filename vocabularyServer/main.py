
from fastapi import FastAPI
from vocabulary.routers import v_router
from periodic_tasks import Task


app = FastAPI()

task = Task()
task.start()

app.include_router(v_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
