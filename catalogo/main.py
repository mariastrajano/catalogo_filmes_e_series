resp = 0

while resp != 5:
    print("")
    print("CATÁLOGO DE FILMES E SÉRIES")
    print("[1] Registro de Mídias \n[2] Listas Personalizadas \n[3] Histórico \n[4] Relatórios \n[5] Sair")

    if resp > 5:
        print("Digite um número válido.")
    
    resp = int(input(""))
       