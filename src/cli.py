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