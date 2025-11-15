from flask import Flask, request, jsonify, redirect
from settings import secret, CLIENT_ID, CLIENT_SECRET
from database import store_auth
import jwt, time
import requests
from flask_cors import CORS

uris = {
    "dev": "http://localhost:3000",
    "prod": "https://nhdiscord.com"
}

current_uri = uris.get('prod')

def get_user(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    return response.json()

def discord_exchange(exchange_code:str):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': exchange_code,
        'redirect_uri': f"{current_uri}/authorize"
    }
    response = requests.post('https://discord.com/api/v10/oauth2/token', data=data)
    return response.json()


app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return "welcome to the api!"


@app.route('/authorize', methods=["POST"])
def authorize():
    print("Call made!")
    authorization_code = request.args.get('code')
    if not authorization_code:
        return jsonify({"success": False, "message":"No code provided in uri"})
    exchange_info:dict = discord_exchange(authorization_code)
    print(exchange_info)
    error = exchange_info.get('error')
    if error:
        return jsonify({"success": False, "message":exchange_info.get("error_description")})
    access_token = exchange_info.get('access_token')
    user_info:dict = get_user(access_token)
    user_id = user_info.get('id')
    database_id = store_auth(user_id, exchange_info)

    response = jsonify({
        "success": True,
        "user_info": user_info,
        "token": str(database_id)
    })
    return response

@app.route('/authorize/get')
def api_get_user():
    auth_token = request.args.get('token')
    return jsonify({"success": True})

app.run(debug=True)