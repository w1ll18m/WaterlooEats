import os
import jwt
import requests
from dotenv import load_dotenv

load_dotenv()

class Auth0Client:
    def __init__(self):
        self.issuer_url = None
        self.audience = None
        self.algorithm = "RS256"
        self.jwks_uri = None
    
    def initialize(self, auth0_domain, auth0_audience):
        self.issuer_url = f"https://{auth0_domain}/"
        self.audience = auth0_audience
        self.jwks_uri = f"{self.issuer_url}.well-known/jwks.json"
    
    def get_signing_key(self, token):
        jwks_client = jwt.PyJWKClient(self.jwks_uri)
        return jwks_client.get_signing_key_from_jwt(token).key

def validate_auth0_token(token):
    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.exceptions.DecodeError:
        return False
    
    auth0_client = Auth0Client()
    auth0_client.initialize(os.getenv("AUTH0_DOMAIN"), os.getenv("AUTH0_AUDIENCE"))
    signing_key = auth0_client.get_signing_key(token)

    try:
        decoded_token = jwt.decode(
            token, 
            signing_key, 
            algorithms=["RS256"], 
            audience=auth0_client.audience,
            issuer=auth0_client.issuer_url
        )
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

    return decoded_token

def get_management_api_token():
    domain = os.getenv("AUTH0_DOMAIN")
    url = f"https://{domain}/oauth/token"
    payload = {
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
        "client_secret": os.getenv("AUTH0_CLIENT_SECRET"),
        "audience": os.getenv("AUTH0_AUDIENCE"),
        "grant_type": "client_credentials"
    }
    response = requests.post(url, json=payload)

    return response.json()["access_token"]