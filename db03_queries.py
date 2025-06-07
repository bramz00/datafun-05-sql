import sqlite3

DB_FILE = "C:/Repos/datafun-05-sql/datafun.db"
SQL_DIR = "C:/Repos/datafun-05-sql/sql_queries"

SQL_FILES = [
    "query_aggregation.sql",
    "query_filter.sql",
    "query_sorting.sql",
    "query_group_by.sql",
    "query_join.sql"
]

def run_queries():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        for file_name in SQL_FILES:
            file_path = f"{SQL_DIR}/{file_name}"
            print(f"\n--- Running {file_name} ---\n")

            with open(file_path, "r", encoding="utf-8") as f:
                sql_script = f.read()

            statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
            for stmt in statements:
                cursor.execute(stmt)
                if stmt.lower().startswith("select"):
                    rows = cursor.fetchall()
                    if rows:
                        col_names = [desc[0] for desc in cursor.description]
                        print(f"Columns: {col_names}")
                        for row in rows:
                            print(row)
                    else:
                        print("No rows returned.")
            print("\n--------------------------")

    except Exception as e:
        print(f"Error executing queries: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_queries()
