import motor.motor_asyncio
import certifi
import json


# Load cluster url từ file json
with open("./config.json", "r") as file:
    config = json.load(file)


MONGODB_URL = config["cluster"]
DATABASE_NAME = "top100-nct"


async def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL, tlsCAFile=certifi.where())
    return client[DATABASE_NAME]
