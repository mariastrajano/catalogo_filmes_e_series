import os
from midia import Midia

"""
Interface de linha de comando da aplicação.
"""

resp = 0

while resp != 5:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("CATÁLOGO DE FILMES E SÉRIES")
    print("[1] Registro de Mídias \n[2] Listas Personalizadas \n[3] Histórico \n[4] Relatórios \n[5] Sair")

    resp = int(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')

    if resp == 1:
        resp_midia = 0

        while resp_midia != 3:
            print("REGISTRO DE MÍDIA")
            print("[1] Adicinar nova mídia \n[2] Modificar mídia existente \n[3] Voltar para o menu")

            resp_midia = int(input(""))
            os.system('cls' if os.name == 'nt' else 'clear')


            if resp_midia == 1:
                print("NOVA MÍDIA")
                titulo = input("Título: ").upper()
                tipo = input("Tipo (Filme ou Série): ").upper()
                genero = input("Gênero: ").upper()
                ano = int(input("Ano: "))
                duracao = int(input("Duração (em min): "))
                classificacao_indicativa = input("Classificação Indicativa (L, 10, 12, 14, 16 ou 18): ").upper()
                elenco = input("Elenco: ").upper()
                status = input("Status: ").upper()
                nota = float(input("Nota: "))

                midia = Midia(titulo, tipo, genero, ano, duracao, classificacao_indicativa, elenco, status, nota)

            elif resp_midia == 2:
                print("MODIFICAR MÍDIA")
                novo_status = input("Digite o novo status da mídia: ")
                midia.atualizar_status(novo_status)

            print(vars(midia))