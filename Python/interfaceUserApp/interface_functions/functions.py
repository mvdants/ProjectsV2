import json
from typing import Union, Literal


users_file = "../users/users.json"


def create_user(user: dict) -> None:
    users = read_json_file()
    users.append(user)
    users = write_json_file(users)


def read_json_file() -> list:
    with open(users_file, 'r') as f:
        users = json.load(f)
        f.close()
    return users


def write_json_file(all_users: list) -> list:
    with open(users_file, 'w', encoding="utf-8") as f:
        json.dump(all_users, f, ensure_ascii=False, indent=4, separators=(",", ":"))
        f.close()
    return all_users


if __name__ == '__main__':
    print("testing")
    sarah = {
        "id": len(read_json_file()),
        "name": "Sarah",
        "surname": "DANTAS"
    }
    create_user(sarah)
