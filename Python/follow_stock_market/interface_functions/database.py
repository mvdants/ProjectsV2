"""
File Python unused...
I am still studying this SQL ...
https://www.freecodecamp.org/news/connect-python-with-sql/
"""


import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("SUCCESSFUL!!")
    except Error as err:
        print(f'Error {err}')

    return connection


if __name__ == '__main__':
    connect = create_server_connection("localhost", "root", "123456")
