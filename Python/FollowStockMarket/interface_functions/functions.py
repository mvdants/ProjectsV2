import json
from typing import Union, Tuple


users_file = "../data/users.json"
Email = str


def create_user(user: dict) -> None:
    users = read_json_file()
    users.append(user)
    write_json_file(users)


def read_json_file() -> list:
    with open(users_file, 'r') as f:
        users = json.load(f)
        f.close()
    return users


def write_json_file(all_users: list) -> None:
    with open(users_file, 'w', encoding="utf-8") as f:
        json.dump(all_users, f, ensure_ascii=False, indent=4, separators=(",", ":"))
        f.close()


def get_all_user_email() -> list:
    """Getting all email registered and making a list"""
    return [user["email"] for user in read_json_file()]


def verify_user(user_email: str, user_password: str) -> Tuple[bool, bool]:

    # Getting all email registered and making a list
    users_email: list = get_all_user_email()

    # Getting all password registered and making a list
    users_password: list = [user["password"] for user in read_json_file()]

    # Making a dict which the keys are the emails and the values are the passwords
    email_password: dict = dict(zip(users_email, users_password))

    # Getting the email from the list if exist
    email: Union[str, None] = verify_email_exist(list(email_password.keys()), user_email)

    # Getting the password from the dict if exist
    password: Union[str, None] = email_password[email] if email is not None else None

    # Making the return : if we had a good user with the correct email and password
    if email == user_email and password == user_password:
        return True, True

    # Making the return : if we had a bad user with the correct email but wrong password
    elif email == user_email and password != user_password:
        return True, False

    # Making the return : if we had a bad user with the wrong email
    else:
        return False, False


def verify_email_exist(emails: list, email_target: str) -> Union[Email, None]:
    for email in emails:
        if email == email_target:
            return email
        else:
            return None


if __name__ == '__main__':
    print(verify_user("miguelvitordantas@gmail.com", "123456"))
