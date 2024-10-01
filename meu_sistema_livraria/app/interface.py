import os
from pathlib import Path
import sys
from create_database import create_livros_table
from CRUD import connect_db, add_livro, get_livros, att_preço, remove_livro, buscar_livro_titulo, buscar_livro_id, buscar_livro_ano, buscar_livro_autor, buscar_livro_preço, sync_database_with_csv
from export_csv import add_livro_csv, remove_livro_csv

base_dir = Path(__file__).resolve().parent.parent.parent
db_path = base_dir / "meu_sistema_livraria" / "data" / "livros.db"

conn = connect_db(db_path)
create_livros_table(conn)

# menusinho com os comandos, se quiser usa Tkinter para fazer uma interface grafica(ja q tu gosta dessas coisa)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------Livraria------")
    print("--------------------")
    print("")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Atualizar preço")
    print("4 - Remover livro")
    print("5 - Buscar livro")
    print("6 - Atualizar database")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1": # 1 - Adicionar livro
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---Adicionar livro---")
        print("---------------------")
        print("")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        preço = float(input("Preço: "))
        add_livro(conn, titulo, autor, ano, preço)
        add_livro_csv(conn)

    elif op == "2": # 2 - Listar livros
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---Listar livros---")
        print("-------------------")
        print("")
        livros = get_livros(conn)
        for livro in livros:
            print(livro)


        print("")
        print("0 - Voltar")
        print("1 - Sair")

        op = input("Escolha uma opção: ")
        if op =="0":
                continue
        if op == "1":
            sys. exit()

    elif op == "3": # 3 - Atualizar preço
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---Atualizar preço---")
        print("----------------------")
        print("")
        id = int(input("ID: "))
        preço = float(input("Preço: "))
        att_preço(conn, id, preço)

    elif op == "4": # 4 - Remover livro
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---Remover livro---")
        print("-------------------")
        print("")
        id = int(input("ID: "))
        remove_livro(conn, id)
        remove_livro_csv(id)

    elif op == "5": # 5 - Buscar livro
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---Buscar livro---")
        print("------------------")
        print("")
        print("1 - Título")
        print("2 - Autor")
        print("3 - Ano")
        print("4 - Preço")
        print("5 - ID")
        print("6 - Voltar")
        op_busca = input("escolha uma opçao:")

        if op_busca == "1": # 1 - Título
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Buscar por título---")
            print("------------------------")
            print("")
            titulo = input("Título: ")
            livros = buscar_livro_titulo(conn, titulo)
            print(livros)

            
            print("")
            print("0 - Voltar")
            print("1 - Sair")

            op = input("Escolha uma opção: ")
            if op =="0":
                continue
            if op == "1":
                sys. exit()

        elif op_busca == "2": # 2 - Autor
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Buscar por autor---")
            print("-----------------------")
            print("")
            autor = input("Autor: ")
            livros = buscar_livro_autor(conn, autor)
            print(livros)
            
            
            print("")
            print("0 - Voltar")
            print("1 - Sair")

            op = input("Escolha uma opção: ")
            if op =="0":
                continue
            if op == "1":
                sys. exit()

        elif op_busca == "3": # 3 - Ano
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Buscar por ano---")
            print("---------------------")
            print("")
            ano = int(input("Ano: "))
            livros = buscar_livro_ano(conn, ano)
            print(livros)
            
            
            print("")
            print("0 - Voltar")
            print("1 - Sair")

            op = input("Escolha uma opção: ")
            if op =="0":
                continue
            if op == "1":
                sys. exit()

        elif op_busca == "4": # 4 - Preço
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Buscar por preço---")
            print("-----------------------")
            print("")
            preço = float(input("Preço: "))
            livros = buscar_livro_preço(conn, preço)
            print(livros)
            
            
            print("")
            print("0 - Voltar")
            print("1 - Sair")

            op = input("Escolha uma opção: ")
            if op =="0":
                continue
            if op == "1":
                sys. exit()

        elif op_busca == "5": # 5 - ID
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---Buscar por id---")
            print("--------------------")
            print("")
            id = int(input("ID: "))
            livros = buscar_livro_id(conn, id)
            print(livros)
            
            
            print("")
            print("0 - Voltar")
            print("1 - Sair")

            op = input("Escolha uma opção: ")
            if op =="0":
                continue
            if op == "1":
                sys. exit()

        elif op_busca == "6": # 6 - Voltar"
            continue
        else:
            print("Opção inválida")

    elif op == "6": # 6 - Atualizar database
        sync_database_with_csv(conn)

    elif op == "0": # 0 - Sair
        sys. exit()
    else:
        print("Opção inválida")
    print("")