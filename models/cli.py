import os

from data.dados import Dados
from models.usuario import Usuario
from models.relatorio import Relatorio
from models.historico import Historico

class Cli:
    def __init__(self):
        self.catalogo()

    def limpar_tela(self):
        menu = input("Pressione Enter para continuar... ")
        os.system('cls' if os.name == 'nt' else 'clear')

    def catalogo(self):

        resp = 0
        
        u = Usuario()
        h = Historico()
        r = Relatorio()
        d = Dados()

        while resp != 5:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("=== CATÁLOGO DE FILMES E SÉRIES ===")
            print("[1] Registro de Mídias")
            print("[2] Listas Personalizadas")
            print("[3] Histórico")
            print("[4] Relatórios")
            print("[5] Sair")

            resp = int(input("Selecione uma opção (1-5): "))
            os.system('cls' if os.name == 'nt' else 'clear')

            # -------------------
            # REGISTTO DE MÍDIAS
            # -------------------

            if resp == 1:

                resp_midia = 0
                while resp_midia !=3:

                    print("=== REGISTRO DE MÍDIA ===")
                    print("[1] Adicionar Mídia")
                    print("[2] Listar Mídias")
                    print("[3] Voltar")

                    resp_midia = int(input("Selecione uma opção (1-3): "))
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if resp_midia == 1:
                        u.adicionar_midia()

                    elif resp_midia == 2:
                        u.listar_midias()
                        self.limpar_tela()

                    else:
                        print("Opção Inválida!")

            # -------------------
            # LISTAS PERSONALIZADAS
            # -------------------

            elif resp == 2:

                resp_lista = 0

                while resp_lista != 5:

                    print("=== LISTAS PERSONALIZADAS ===")
                    print("[1] Criar nova lista")
                    print("[2] Adicionar mídia em lista")
                    print("[3] Remover mídia em lista")
                    print("[4] Listar listas")
                    print("[5] Voltar")

                    resp_lista = int(input("Selecione uma opção (1-4): "))
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if resp_lista == 1:
                        u.criar_lista()

                    elif resp_lista == 2:
                        u.adicionar_midia_lista()
                        self.limpar_tela()

                    elif resp_lista == 3:
                        u.remover_midia_lista()
                        self.limpar_tela()

                    elif resp_lista == 4:
                        u.listar_listas()
                        self.limpar_tela()

                    else:
                        print("Opção Inválida!")

            # -------------------
            # HISTÓRICO
            # -------------------

            if resp == 3:
                
                resp_hist = 0
                while resp_hist !=3:

                    print("=== HISTÓRICO ===")
                    print("[1] Ocupação por semana")
                    print("[2] Ocupação por mês")
                    print("[3] Voltar")

                    resp_hist = int(input("Selecione uma opção (1-3): "))
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if resp_hist == 1:
                        h.ocupacao_por_semana()
                        self.limpar_tela()

                    elif resp_hist == 2:
                        h.ocupacao_por_mes()
                        self.limpar_tela()

                    else:
                        print("Opção Inválida!")

            # -------------------
            # RELATÓRIOS
            # -------------------

            elif resp == 4:

                resp_rel = 0

                while resp_rel != 4:

                    print("=== RELATÓRIOS ===")
                    print("[1] Média das notas por gênero")
                    print("[2] Tempo assistido por tipo")
                    print("[3] Top 10 Filme/Séries")
                    print("[4] Voltar")

                    resp_rel = int(input("Selecione uma opção (1-4): "))
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if resp_rel == 1:
                        r.media_notas_por_genero()
                        self.limpar_tela()

                    elif resp_rel == 2:
                        r.tempo_total_assistido()
                        self.limpar_tela()

                    elif resp_rel == 3:
                        r.top_10()
                        self.limpar_tela()

                    else:
                        print("Opção Inválida!")

            else:
                print("Opção Inválida!")