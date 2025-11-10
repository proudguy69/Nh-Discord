from flask import Flask, request, jsonify, redirect
from settings import secret, CLIENT_ID, CLIENT_SECRET
from database import store_auth
import jwt, time
import requests


def create_session_token(user_id:int):
    payload = {
        "user_id": user_id,
        "initiated_at": int(time.time()),
        "expires": int(time.time()) + 60*60*24*7
    }
    return jwt.encode(payload, secret, algorithm="HS256")

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
        'redirect_uri': "https://api.nhdiscord.com/authorize"
    }
    response = requests.post('https://discord.com/api/v10/oauth2/token', data=data)
    return response.json()


app = Flask(__name__)

@app.route('/')
def index():
    return "welcome to the api!"


@app.route('/authorize')
def authorize():
    authorization_code = request.args.get('code')
    if not authorization_code:
        return jsonify({"status": "failed", "message":"No code provided in uri"})
    exchange_info:dict = discord_exchange(authorization_code)
    access_token = exchange_info.get('access_token')
    user_info:dict = get_user(access_token)
    user_id = user_info.get('id')
    session_token = create_session_token(user_id)
    store_auth(user_id, exchange_info, session_token)
    print(session_token)
    response = redirect("http://localhost:3000/")
    response.set_cookie("session", session_token, domain="http://localhost:3000")
    return response

@app.route('/get/user')
def api_get_user():
    print(request.cookies)
    return jsonify({"success": True})

app.run(debug=True)