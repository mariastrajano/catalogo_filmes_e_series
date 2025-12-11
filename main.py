import os
from models.catalogo import Catalogo
from models.relatorio import Relatorio

resp = 0

while resp != 5:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=== CATÁLOGO DE FILMES E SÉRIES ===")
    print("[1] Registro de Mídias \n[2] Listas Personalizadas \n[3] Histórico \n[4] Relatórios \n[5] Sair")

    resp = int(input("Selecione uma opção (1-5): "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if resp == 1:
        
        resp_midia = 0
        c = Catalogo()

        while resp_midia !=3:

            print("=== REGISTRO DE MÍDIA ===")
            print("[1] Adicionar Nova Mídia \n[2] Listar Mídias \n[3] Voltar para o Menu")

            resp_midia = int(input("Selecione uma opção (1-3): "))
            os.system('cls' if os.name == 'nt' else 'clear')

            if resp_midia == 1:
                c.adicionar_midia()

            elif resp_midia == 2:
                c.listar_midias()

            else:
                print("Opção Inválida!")

    elif resp == 3:

        resp_historico = 0

        print("=== HISTÓRICO ===")
        print("")

    elif resp == 4:

        resp_relatorio = 0
        r = Relatorio()
        
        while resp_relatorio !=5:

            print("=== RELATÓRIOS ===")
            print("[1] Média das notas por gênero \n[2] Tempo assistido por tipo \n[3] Top 10 Filmes/Séries \n[4] Ocupação por Período \n[5] Voltar para o Menu")

            resp_relatorio = int(input("Selecione uma opção (1-5): "))
            os.system('cls' if os.name == 'nt' else 'clear')

            if resp_relatorio == 1:
                r.media_nota_genero()
            elif resp_relatorio == 2:
                r.tempo_total_assistido()
            elif resp_relatorio == 3:
                r.top_10()
            elif resp == 4:
                pass
            else:
                print("Opção Inválida!.")