import os
import sqlite3
from midia import Midia

class Usuario:
    """
    Representa um usuário do sistema.
    Gerencia listas personalizadas e histórico.
    """
    def __init__(self):
        self.midias = []

    # Métodos

    def adicionar_midia(self):
        while True:
            print("NOVA MÍDIA")

            titulo = input("Título: ").upper()
            tipo = input("Tipo (Filme ou Série): ").upper()
            genero = input("Gênero: ").upper()
            ano = int(input("Ano de Lançamento: "))
            classificacao = input("Classificação Indicativa (L, 10, 12, 14, 16 ou 18): ").upper()
            elenco = input("Elenco: ").upper()
            status = input("Status: ").upper()

            midia = Midia(titulo, tipo, genero, ano, classificacao, elenco, status)
            self.midias.append(midia)

            cursor.execute("INSERT INTO midia VALUES ('"+titulo+"', '"+tipo+"', '"+genero+"', '"+str(ano)+"', '"+classificacao+"', '"+elenco+"', '"+status+"')")
            banco.commit()

            resp = input("Deseja adicionar outra mídia? (S/N) ").upper()
            if resp == "N": 
                break

            os.system('cls' if os.name == 'nt' else 'clear')