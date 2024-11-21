import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    height TEXT,
    weight TEXT
    )
''')
connection.commit()

def create_user(username, age, height, weight):
    """
    This function will allow creating a new user
    by storing their username, age, height, and weight in the database.

    :param username: The name of the user (str).
    :param age: The age of the user (int).
    :param height: The height of the user in centimeters (int).
    :param weight: The weight of the user in kilograms (int).
    """

    cursor.execute('INSERT INTO users (username, age, height, weight) VALUES (?, ?, ?, ?)', (username, age, height, weight))
    connection.commit()

    print("\nUtilizador registado com sucesso!\n")
