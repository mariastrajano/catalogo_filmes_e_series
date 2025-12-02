import os
from src.episodio import Episodio

class Temporada:
    """
    Representa uma temporada de uma série.
    """
    def __init__(self, numero):
        self.numero = numero
        self.episodios = []

# Encapsulamento
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if numero <= 0:
            raise ValueError("Número de episódios deve ser positivo.")
        else:
            self._numero = numero
    
# Métodos

    def adicionar_episodio(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOVO EPISÓDIOS")
            
            numero = int(input("Número: "))
            titulo = input("Título: ").upper()
            duracao = int(input("Duração (em mim): "))
            status = input("Status: ").upper()
            nota = float(input("Nota: "))

            episodio = Episodio(numero, titulo, duracao, status, nota)
            self.episodios.append(episodio)

            resp = input("Deseja adicionar outra episódio? (S/N) ").upper()
            if resp == "N": 
                break

    def total_episodios(self):
        return sum(+ 1 for episodio in self.episodios)
    
    def listar_episodios(self):
        print(f"TEMPORADA {self.numero}: ")
        for episodio in self.episodios:
            print(f"{episodio.numero} - {episodio.titulo}")
