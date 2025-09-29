import sqlite3

def transaction_manager(sql_command, parameter_list=None, commit=False):
    connection = sqlite3.connect('./model/repository/finance.db')
    cursor = connection.cursor()
    if parameter_list:
        cursor.execute(sql_command, parameter_list)
    else:
        cursor.execute(sql_command)
    if commit:
        connection.commit()
        result_list = parameter_list
    else:
        result_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return result_list

def create_database():
    connection = sqlite3.connect('./model/repository/finance.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    """)

    cursor.close()
    connection.close()
