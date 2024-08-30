from fastapi import FastAPI

from .routers import samurai

app = FastAPI(title='Samurai', version='0.1.0')

app.include_router(samurai.router)