import sqlite3

DB_FILE = "C:/Repos/datafun-05-sql/datafun.db"
SQL_DIR = "C:/Repos/datafun-05-sql/sql_create"

SQL_FILES = [
    "01_drop_tables.sql",
    "02_create_tables.sql",
    "03_insert_records.sql"
]

def run_sql_scripts():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        for file_name in SQL_FILES:
            file_path = SQL_DIR + "/" + file_name
            print(f"Executing {file_name}...")
            with open(file_path, "r", encoding="utf-8") as f:
                sql = f.read()
                cursor.executescript(sql)
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Initialization did not complete: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_sql_scripts()
