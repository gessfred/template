from fastapi import FastAPI 
from routers import example

app = FastAPI()

app.include_router(example.router)

