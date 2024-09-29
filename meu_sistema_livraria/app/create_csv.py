import csv
from pathlib import Path

# Caminho do arquivo CSV
base_dir = Path(__file__).resolve().parent.parent
path_csv = base_dir / "exports" / "livros_exportados.csv"

# Função para adicionar um livro ao CSV
def add_livro_csv(conn):
    # Recupera todos os livros do banco de dados
    livros = conn.execute("SELECT * FROM livros").fetchall()

    # Recupera o último livro adicionado (usando o maior ID)
    ultimo_livro = conn.execute("SELECT * FROM livros ORDER BY id DESC LIMIT 1").fetchone()

    # Verifica se o arquivo CSV já existe
    csv_existe = path_csv.exists()

    if csv_existe:
        with open(path_csv, mode='a', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)

            escritor_csv.writerow(ultimo_livro)

    else:
        with open(path_csv, mode='w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
        
            escritor_csv.writerow(['ID', 'Titulo', 'Autor', 'Ano', 'Preco'])

            for livro in livros:
                escritor_csv.writerow(livro)



# Função para remover um livro do CSV
def remove_livro_csv(livro_id):
    if not path_csv.exists():
        return
    
    livros = []
    
    # Ler todos os livros do CSV
    with open(path_csv, mode='r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        cabecalho = next(reader)  # Ler o cabeçalho
        livros = [linhas for linhas in reader if linhas and int(linhas[0]) != livro_id]  # Excluir o livro com o ID fornecido

    # Reescrever o arquivo CSV sem o livro removido
    with open(path_csv, mode='w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(cabecalho)  # Reescrever o cabeçalho
        escritor_csv.writerows(livros)  # Escrever os livros restantes

