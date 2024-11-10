from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # Carga variables de entorno desde .env

app = FastAPI()

# Configuración de autenticación en Spotify
SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://localhost:8000/login/callback"

spotify_oauth = SpotifyOAuth(
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
    scope="user-library-read playlist-modify-private",
    cache_path=".spotifycache",
)

# Endpoint para iniciar el flujo de autenticación
@app.get("/login")
async def login_spotify():
    authorization_url = spotify_oauth.get_authorize_url()
    return {"Authorization URL": authorization_url}

# Callback para manejar la respuesta de Spotify después de la autenticación
@app.get("/login/callback")
async def login_callback(code: str):
    token_info = spotify_oauth.get_access_token(code)
    return {"access_token": token_info["access_token"]}