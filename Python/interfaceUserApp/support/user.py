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


if __name__ == '__main__':
    miguel = User("Miguel", "MACEDO DANTAS", "26-08-1999", "M", "miguelvitordantas@gmail.com", "123456")
    create_user(miguel.user2json())
    print(read_json_file())
