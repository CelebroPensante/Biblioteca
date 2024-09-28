import sqlite3
from pathlib import Path

def connect_db(db_path):
    return sqlite3.connect(db_path)
    print("Connected to database") #debug 

def create_livros_table(conn):
    with conn:
        conn.execute("""
            CREATE TABLE livros (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER NOT NULL,
                preço REAL NOT NULL
            )
        """)
        print("Table created") #debug
        
db_path = Path("DataBase/livros.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

conn = connect_db(db_path)
create_livros_table(conn)
conn.close()