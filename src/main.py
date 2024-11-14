from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables de entorno desde .env

app = FastAPI()

@app.get("/")
async def read_post():
    return {"mensaje": "Hoy arranca ZettaSimIA!!"}

