import sqlite3
from pathlib import Path
from backup_generator import create_backup

def connect_db(db_path):
    return sqlite3.connect(db_path)
    print("Connected to database") #debug
    
# faz o crud com as interações que o professor pediu e mais algumas
# se quiser da pra fazer uma pasta crud com os arquivos separados para 
# facilitar manutenção e ficar mais organizado, mas nao acho necessario

# adiciona um livro
def add_livro(conn, titulo, autor, ano, preço):
    create_backup()
    with conn:
        conn.execute("""
            INSERT INTO livros (titulo, autor, ano, preço)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, preço))
        print("Livro added") #debug
        
# pega todos os livros
def get_livros(conn):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
        """).fetchall()

# atualiza o preço de um livro
def att_preço(conn, id, preço):
    create_backup()
    with conn:
        conn.execute("""
            UPDATE livros
            SET preço = ?
            WHERE id = ?
        """, (preço, id))
        print("Preço updated") #debug
        
# remove um livro
def remove_livro(conn, id):
    create_backup()
    with conn:
        conn.execute("""
            DELETE FROM livros
            WHERE id = ?
        """, (id,))
        print("Livro removed") #debug

# busca um livro por titulo
def buscar_livro_titulo(conn, titulo):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE titulo = ?
        """, (titulo,)).fetchall()

# busca um livro por autor
def buscar_livro_autor(conn, autor):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE autor = ?
        """, (autor,)).fetchall()

# busca um livro por ano
def buscar_livro_ano(conn, ano):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE ano = ?
        """, (ano,)).fetchall()

# busca um livro por preço
def buscar_livro_preço(conn, preço):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE preço = ?
        """, (preço,)).fetchall()

# busca um livro por id
def buscar_livro_id(conn, id):
    create_backup()
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE id = ?
        """, (id,)).fetchall()