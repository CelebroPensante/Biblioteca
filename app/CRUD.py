import sqlite3
from pathlib import Path

def connect_db(db_path):
    return sqlite3.connect(db_path)
    print("Connected to database") #debug
    
def add_livro(conn, titulo, autor, ano, preço):
    with conn:
        conn.execute("""
            INSERT INTO livros (titulo, autor, ano, preço)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, preço))
        print("Livro added") #debug
        
def get_livros(conn):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
        """).fetchall()

def att_preço(conn, id, preço):
    with conn:
        conn.execute("""
            UPDATE livros
            SET preço = ?
            WHERE id = ?
        """, (preço, id))
        print("Preço updated") #debug
        
def remove_livro(conn, id):
    with conn:
        conn.execute("""
            DELETE FROM livros
            WHERE id = ?
        """, (id,))
        print("Livro removed") #debug
        
def buscar_livro_titulo(conn, titulo):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE titulo = ?
        """, (titulo,)).fetchall()

def buscar_livro_autor(conn, autor):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE autor = ?
        """, (autor,)).fetchall()
        
def buscar_livro_ano(conn, ano):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE ano = ?
        """, (ano,)).fetchall()
        
def buscar_livro_preço(conn, preço):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE preço = ?
        """, (preço,)).fetchall()
        
def buscar_livro_id(conn, id):
    with conn:
        return conn.execute("""
            SELECT * FROM livros
            WHERE id = ?
        """, (id,)).fetchall()