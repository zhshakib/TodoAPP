from fastapi import FastAPI
from routers.todos import router


app = FastAPI()

app.include_router(router)
