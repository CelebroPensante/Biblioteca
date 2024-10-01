import sqlite3
import csv
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
    
def sync_database_with_csv(conn):
    # Caminho do arquivo CSV
    base_dir = Path(__file__).resolve().parent.parent
    path_csv = base_dir / "exports" / "livros_exportados.csv"

    # Verifica se o arquivo CSV existe
    if not path_csv.exists():
        print("Arquivo CSV não encontrado")
        return

    # Lê os dados do CSV
    with open(path_csv, mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        cabecalho = next(reader)  # Ignora o cabeçalho

        for linha in reader:
            id_csv, titulo, autor, ano, preco = linha

            # Verifica se o livro já existe no banco de dados
            livro_existente = conn.execute("""
                SELECT * FROM livros WHERE id = ?
            """, (id_csv,)).fetchone()

            if livro_existente:
                print(f"Livro com ID {id_csv} já está no banco de dados, pulando...")
            else:
                # Se não existir, insere no banco de dados
                conn.execute("""
                    INSERT INTO livros (id, titulo, autor, ano, preço)
                    VALUES (?, ?, ?, ?, ?)
                """, (id_csv, titulo, autor, int(ano), float(preco)))
                print(f"Livro com ID {id_csv} adicionado ao banco de dados")

    conn.commit()