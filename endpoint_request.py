import json
import os
import time

import requests
from dotenv import load_dotenv

##append endpoint before
base_url = "http://localhost:8080/api/"

bearer_token: str = ""
expire_date: float = 0


def get_headers():
    return {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }


# pass unique value
async def add_post(user_id: str, content: str):
    #    if not check_if_token_expire():
    response = requests.post(base_url + "test/addPost", headers=get_headers(), json={
        "testUserId": user_id,
        "testContent": content
    })

    match response.status_code:
        case 200:
            print("successfully post added.")
        case 201:
            print("successfully post added.")
        case _:
            print(f"exception f{response.status_code} ->{response.text}")


# auth/register
async def register_request():
    load_dotenv()
    response = requests.post(base_url + "auth/register", json={
        "userName": f"{os.getenv('USERNAME')}",
        "password": f"{os.getenv('PASSWORD')}",
        "email": f"{os.getenv('EMAIL')}"
    })


##auth/login
async def login_request():
    global bearer_token
    global expire_date

    response = requests.post(base_url + "auth/login", json={
        "userName": f"{os.getenv('USER_NAME')}",
        "password": f"{os.getenv('PASSWORD')}",
        "email": f"{os.getenv('EMAIL')}"
    })

    data = json.loads(response.text)

    bearer_token = data["token"]

    # ms
    expire_date = int(time.time() * 1000) + int(data["expiresIn"])

    # todo check if token expired than re-login

# parse json here and take bearer-token to re-use

# async def addpost_request():
