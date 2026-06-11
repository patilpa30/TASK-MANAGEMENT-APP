from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import router
from src.user.router import user_router

Base.metadata.create_all(engine)
app = FastAPI(
    title="Task Management Application"
)
app.include_router(router)
app.include_router(user_router)

