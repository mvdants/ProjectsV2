"""
Creating a multiple list of user randomly
"""
import requests
from support.user import User
from typing import List


def creating_single_user() -> User:
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user = response.json()
        return User(
            name=user["results"][0]["name"]["first"],
            surname=user["results"][0]["name"]["last"],
            birthday=user["results"][0]["dob"]["date"],
            gender=user["results"][0]["gender"],
            email=user["results"][0]["email"],
            password=user["results"][0]["login"]["password"]
        )
    else:
        raise ConnectionError("Some problem to connect to the API server")


def creating_multiple_users(number: int) -> List[User]:
    response = requests.get(f"https://randomuser.me/api/?results={number}")
    if response.status_code == 200:
        user = response.json()
        user_list = []
        for i in range(len(user["results"])):
            user_list.append(User(
                name=user["results"][i]["name"]["first"],
                surname=user["results"][i]["name"]["last"],
                birthday=user["results"][i]["dob"]["date"],
                gender=user["results"][i]["gender"],
                email=user["results"][i]["email"],
                password=user["results"][i]["login"]["password"]
            ))
        return user_list
    else:
        raise ConnectionError("Some problem to connect to the API server")


if __name__ == '__main__':
    u = creating_single_user()
    print(u.user2json())
