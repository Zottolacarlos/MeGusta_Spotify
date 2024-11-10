from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables de entorno desde .env

app = FastAPI()