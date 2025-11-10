from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
database = client.get_database('manofthemountain')
authorization = database.get_collection('authorization')

def store_auth(user_id, bearer_data, session_token):
    authorization.update_one(
        {"session_token":session_token},
        {"$set":{
            "user_id": user_id,
            "bearer_data": bearer_data,
            "session_token": session_token
        }},
        upsert=True)
    
