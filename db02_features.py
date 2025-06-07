import sqlite3

DB_FILE = "C:/Repos/datafun-05-sql/datafun.db"
SQL_DIR = "C:/Repos/datafun-05-sql/sql_features"

SQL_FILES = [
    "update_records.sql",
    "delete_records.sql"
]

def run_sql_scripts():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        for file_name in SQL_FILES:
            file_path = f"{SQL_DIR}/{file_name}"
            print(f"Executing {file_name}...")
            with open(file_path, "r", encoding="utf-8") as file:
                sql_script = file.read()
                cursor.executescript(sql_script)
        conn.commit()
        print("Update and delete queries executed successfully.")
    except Exception as e:
        print(f"Error executing scripts: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_sql_scripts()
