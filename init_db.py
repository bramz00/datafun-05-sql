import sqlite3

DB_FILE = "C:\Repos\datafun-05-sql\datafun.db"

SQL_FILE = "C:\Repos\datafun-05-sql\create_tables.sql"

def initialize_database():
    connect = sqlite3.connect(DB_FILE)
    cursor = connect.cursor()

    with open(SQL_FILE, "r") as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

    connect.commit()
    connect.close()
    print("Database initialized!")

if __name__ == "__main__":
    initialize_database()
