import requests
from base64 import b64encode

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

# Codificar las credenciales en Base64
credentials = f"{client_id}:{client_secret}"
credentials_base64 = b64encode(credentials.encode('utf-8')).decode('utf-8')

auth_options = {
    'url': 'https://accounts.spotify.com/api/token',
    'headers': {
        'Authorization': 'Basic ' + credentials_base64
    },
    'data': {
        'grant_type': 'client_credentials'
    }
}

response = requests.post(**auth_options)

if response.status_code == 200:
    token = response.json().get('access_token')
    print(f'Token: {token}')
else:
    print(f'Error: {response.status_code}')
    print(response.text)