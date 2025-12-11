import os
from models.filme import Filme
from models.serie import Serie

import sqlite3
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

class Catalogo():
    """
    Interface do Catálogo
    """
    def __init__(self):
        self.midias = []

    def adicionar_midia(self):
        while True:
            print("=== ADICIONAR MÍDIA ===")

            titulo = input("Título: ").capitalize()
            tipo = input("Tipo (Filme ou Série): ").capitalize()
            genero = input("Gênero: ").capitalize()
            ano = int(input("Ano de Lançamento: "))
            classificacao = input("Classificação Indicativa (L, 10, 12, 14, 16 ou 18): ")
            elenco = input("Elenco: ")
            status = input("Status (Não Assistido, Assistindo ou Assistido): ").capitalize()

            if tipo == "Filme":
                duracao = int(input("Duração (em min): "))

                if status == "Assistido":
                    nota = float(input("Nota (0-10): "))
                else:
                    nota = 0.0

                filme = Filme(titulo, "Filme", genero, ano, duracao, classificacao, elenco, status, nota, None)
                filme.banco_de_dados()
                self.midias.append(filme)

                
            else:
                serie = Serie(titulo, "Série", genero, ano, 0, classificacao, elenco, status, 0, None)
                serie.banco_de_dados()
                self.midias.append(serie)

                temporadas = int(input("Quantidade de Temporadas: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                serie.adicionar_temporadas(temporadas)

                serie.set_duracao()
                serie.set_status()
                serie.set_nota()

            print("")
            print("Mídia adicionada com sucesso!")
            print("")

            resp = input("Deseja adicionar outra mídia? (S/N) ").upper()
            os.system('cls' if os.name == 'nt' else 'clear')

            if resp == "N": 
                break

    def listar_midias(self):
        print("=== MÍDIAS CADASTRADAS ===")

        i = 0
        cursor.execute("SELECT titulo, tipo, ano, status, nota FROM midias WHERE titulo IS NOT NULL")

        for row in cursor:
            i += 1
            print(f"{i}. {row[0]} ({row[1]} - {row[2]}) \n   STATUS: {row[3]} \n   NOTA: {row[4]}")

            print("")
        menu = input("Pressione Enter para continuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

