from interface_functions.functions import create_user, read_json_file


class User:
    def __init__(self, name, surname, birthday, gender, email, password):
        self.__id = len(read_json_file())
        self.__name = name
        self.__surname = surname
        self.__birthday = birthday
        self.__gender = gender
        self.__email = email
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birthday(self):
        return self.__birthday

    @property
    def gender(self):
        return self.__gender

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    def user2json(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "surname": self.__surname,
            "birthday": self.__birthday,
            "gender": self.__gender,
            "email": self.__email,
            "password": self.__password
        }

    @staticmethod
    def json2user(user: dict):
        return User(
            name=user["name"],
            surname=user["surname"],
            birthday=user["birthday"],
            gender=user["gender"],
            email=user["email"],
            password=user["password"]
        )


if __name__ == '__main__':
    miguel = User("Miguel", "MACEDO DANTAS", "26-08-1999", "M", "miguelvitordantas@gmail.com", "123456")
    create_user(miguel.user2json())
    print(read_json_file())
