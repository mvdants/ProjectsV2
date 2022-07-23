"""
Creating a multiple list of user randomly
"""
import requests
from support.user import User
from typing import List
from interface_functions.functions import create_user, read_json_file


def creating_single_user() -> List[User]:
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user = response.json()
        create_user(User(
            name=user["results"][0]["name"]["first"],
            surname=user["results"][0]["name"]["last"],
            birthday=user["results"][0]["dob"]["date"],
            gender=user["results"][0]["gender"],
            email=user["results"][0]["email"],
            password=user["results"][0]["login"]["password"]
        ).user2json())
        return read_json_file()
    else:
        raise ConnectionError("Some problem to connect to the API server")


def creating_multiple_users(number: int = 2) -> List[User]:
    if number < 2:
        creating_single_user()
    elif number < 0:
        raise ValueError("the parameter number have to be positive")
    else:
        response = requests.get(f"https://randomuser.me/api/?results={number}")
        if response.status_code == 200:
            user = response.json()
            for i in range(len(user["results"])):
                create_user(User(
                    name=user["results"][i]["name"]["first"],
                    surname=user["results"][i]["name"]["last"],
                    birthday=user["results"][i]["dob"]["date"],
                    gender=user["results"][i]["gender"],
                    email=user["results"][i]["email"],
                    password=user["results"][i]["login"]["password"]
                ).user2json())
            return read_json_file()
        else:
            raise ConnectionError("Some problem to connect to the API server")


if __name__ == '__main__':
    users = creating_multiple_users(100)
    print(read_json_file())
