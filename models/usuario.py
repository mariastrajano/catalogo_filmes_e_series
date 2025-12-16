import os

from models.filme import Filme
from models.serie import Serie
from models.lista_personalizada import ListaPersonalizada

from data.dados import Dados
from config.settings import Settings

d = Dados()
s = Settings()

class Usuario:
    """
    Representa um usuário do sistema.
    Gerencia mídias e listas personalizadas.
    """
    def __init__(self):
        self.midias = []
        self.listas =[]
        self.carregar_midias()

    # -------------------
    # GERENCIAR MÍDIAS
    # -------------------

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

                if filme in self.midias:
                    raise ValueError("Mídia já cadastrada (título, tipo e ano iguais).")
                else:
                    self.midias.append(filme)
                    d.salvar_filme(filme)

                
            else:
                serie = Serie(titulo, "Série", genero, ano, 0, classificacao, elenco, status, 0.0, None)

                temporadas = int(input("Quantidade de Temporadas: "))
                serie.adicionar_temporadas(temporadas)

                if serie in self.midias:
                    raise ValueError("Série já cadastrada (título, tipo e ano iguais).")
                else:
                    self.midias.append(serie)
                    d.salvar_filme(serie)

            print("")
            print("Mídia adicionada com sucesso!")
            print("")

            resp = input("Deseja adicionar outra mídia? (S/N) ").upper()
            os.system('cls' if os.name == 'nt' else 'clear')

            if resp == "N": 
                break

    def carregar_midias(self):
        self.midias.extend(d.carregar_midias())

    def listar_midias(self):
        print("=== MÍDIAS CADASTRADAS ===")

        if not self.midias:
            print("Catálogo vazio.")
            print("")

        else:
            for i, midia in enumerate(self.midias, 1):
                print(f"{i}. {str(midia)}")
                print("")

    # -------------------
    # GERENCIAR LISTAS PERSONALIZADAS
    # -------------------

    def criar_lista(self):
        while True:
            print("=== NOVA LISTA ===")
            nome = input("Nome da lista: ").capitalize()

            lista = ListaPersonalizada(nome)

            if len(self.listas) >= s.limite_listas:
                raise ValueError("Limite de listas personalizadas atingido.")
            else:
                self.listas.append(lista)

            print("")
            print("Lista criada com sucesso!")
            print("")

            resp = input("Deseja criar outra lista? (S/N) ").upper()
            os.system('cls' if os.name == 'nt' else 'clear')

            if resp == "N": 
                break

    def adicionar_midia_lista(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LISTAS PERSONALIZADAS ===")
        
        for i, lista in enumerate(self.listas, 1):
            print(f"{i}. {lista.nome}")

        print("")
        opcao = int(input("Número da lista: "))
        os.system('cls' if os.name == 'nt' else 'clear')

        lista_escolhida = self.listas[opcao - 1]

        self.listar_midias()
        opcao = int(input("Número da mídia: "))

        midia_escolhida = self.midias[opcao - 1]

        os.system('cls' if os.name == 'nt' else 'clear')
        lista_escolhida.adicionar(midia_escolhida)

    def remover_midia_lista(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LISTAS PERSONALIZADAS ===")
        
        for i, lista in enumerate(self.listas, 1):
            print(f"{i}. {lista.nome}")

        print("")
        opcao = int(input("Número da lista: "))
        os.system('cls' if os.name == 'nt' else 'clear')

        lista_escolhida = self.listas[opcao - 1]

        self.listar_midias()
        opcao = int(input("Número da mídia: "))

        midia_escolhida = self.midias[opcao - 1]

        os.system('cls' if os.name == 'nt' else 'clear')
        lista_escolhida.remover(midia_escolhida)

    def listar_listas(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LISTAS PERSONALIZADAS ===")

        for i, lista in enumerate(self.listas, 1):
                print(f"{i}. {lista.nome}")

        opcao = int(input("Número da lista: "))
        os.system('cls' if os.name == 'nt' else 'clear')

        lista_escolhida = self.listas[opcao - 1]

        lista_escolhida.listar()
