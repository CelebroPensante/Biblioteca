import sqlite3
from pathlib import Path

def connect_db(db_path):
    return sqlite3.connect(db_path)

#criar a tabela livros
def create_livros_table(conn):
    with conn:
        # Verificar se a tabela já existe
        table_exists = conn.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='livros';
        """).fetchone()
        
        if table_exists:
            print("Table 'livros' already exists")
        else:
            conn.execute("""
                CREATE TABLE livros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    preço REAL NOT NULL
                )
            """)
            print("Table 'livros' created")

# Caminho do banco de dados
db_path = Path("../data/livros.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

conn = connect_db(db_path)
create_livros_table(conn)
conn.close()