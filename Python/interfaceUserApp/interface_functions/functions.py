import json
from typing import Union, Literal


users_file = "../users/users.json"


def service_files(file: str, service: Union[Literal["a", "r", "w"]], increment: Union[Literal["+", "-", ""]] = ""):
    def opening_files(function):
        def inner(*args, **kwargs):
            with open(file, service+increment) as f:
                function(*args, **kwargs)
                f.close()
            return function
        return inner
    return opening_files


def create_user(name: str, surname: str) -> None:

    dictionary = {
        "name": name,
        "surname": surname
    }

    with open(users_file, 'a', encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4, separator=",")
        f.close()


def read_json_file():
    with open(users_file, 'r') as f:
        users = json.load(f)
        print(users)
        f.close()
    return users


if __name__ == '__main__':
    # create_user("Lara", "DANTAS")
    user = read_json_file()
    user["users"].append({
        "id": len(user["users"]),
        "name": "Mel",
        "surname": "DANTAS"
    })
    print(user)
