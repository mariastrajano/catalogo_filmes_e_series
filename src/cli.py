import os
from src.filme import Filme
from src.serie import Serie

class Cli():
    """
    Interface de linha de comando da aplicação.
    """

    def __init__(self):
        self.midias = []

    def adicionar_midia(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("---NOVA MÍDIA---")

            titulo = input("Título: ").upper()
            tipo = input("Tipo (Filme ou Série): ").upper()
            genero = input("Gênero: ").upper()
            ano = int(input("Ano de Lançamento: "))
            classificacao = input("Classificação Indicativa (L, 10, 12, 14, 16 ou 18): ").upper()
            elenco = input("Elenco: ").upper()
            status = input("Status (NÃO ASSISTIDO, ASSISTINDO OU ASSISTIDO): ").upper()

            if tipo == "FILME":
                duracao = int(input("Duração (em min): "))
                nota = float(input("Nota: "))
                filme = Filme(titulo, "FILME", genero, ano, classificacao, elenco, status, duracao, nota)
                
                self.midias.append(filme)

            else:
                serie = Serie(titulo, "SERIE", genero, ano, classificacao, elenco, status)
                self.midias.append(serie)

                temporadas = int(input("Quantidade de Temporadas: "))

                os.system('cls' if os.name == 'nt' else 'clear')
                serie.adicionar_temporadas(temporadas)


            resp = input("Deseja adicionar outra mídia? (S/N) ").upper()
            if resp == "N": 
                break

            os.system('cls' if os.name == 'nt' else 'clear')