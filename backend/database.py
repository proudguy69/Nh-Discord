from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
database = client.get_database('manofthemountain')
authorization = database.get_collection('authorization')

def store_auth(user_id, bearer_data):
    authorization.update_one(
        {"user_id":user_id},
        {"$set":{
            "user_id": user_id,
            "bearer_data": bearer_data,
        }},
        upsert=True)
    data:dict = authorization.find_one({"user_id":user_id})

    
    return data.get("_id")
    
