import os
from src.filme import Filme
from src.serie import Serie

class Cli():
    """
    Interface de linha de comando da aplicação.
    """

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
                filme = Filme(titulo, "FILME", genero, ano, duracao, classificacao, elenco, status, nota)

            else:
                serie = Serie(titulo, "SERIE", genero, ano, 1, classificacao, elenco, status, 1)

                temporadas = int(input("Quantidade de Temporadas: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                serie.adicionar_temporadas(temporadas)
                
                serie.set_duracao()
                serie.set_status()
                serie.set_nota()

            resp = input("Deseja adicionar outra mídia? (S/N) ").upper()
            if resp == "N": 
                break

            os.system('cls' if os.name == 'nt' else 'clear')