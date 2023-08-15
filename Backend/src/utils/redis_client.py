import os
import redis
import json
from flask import Response
from dotenv import load_dotenv

load_dotenv()
DEFAULT_EXPIRATION_TIME = 3600

def getOrSetCache(key, cb):
    redis_server_host = os.getenv("REDIS_SERVER_HOST")
    redis_server_port = os.getenv("REDIS_SERVER_PORT")
    redis_client = redis.StrictRedis(host=redis_server_host, port=redis_server_port, db=0)
    existing_data = redis_client.get(key)
    if existing_data is None:
        # print("CACHE MISS") -> FOR TESTING
        fresh_data = cb()
        # if callback function returns a Response object, return it immediately
        if isinstance(fresh_data, Response):
            return fresh_data
        redis_client.setex(key, DEFAULT_EXPIRATION_TIME, json.dumps(fresh_data))
    else:
        # print("CACHE HIT") -> FOR TESTING
        fresh_data = json.loads(existing_data)
    return fresh_data