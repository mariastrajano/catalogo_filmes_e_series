import os
from src.midia import Midia
from src.temporada import Temporada

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota):
        super().__init__(titulo, "SERIE", genero, ano, duracao, classificacao, elenco, status, nota)
        self.temporadas = []

# Encapsulamento

    def set_duracao(self):
        self._duracao = sum(temporada.duracao() for temporada in self.temporadas)

    def set_status(self):
        for temporada in self.temporadas:
            if temporada.episodios_assistidos() == True:
                self._status == "ASSISTIDO"

    def set_nota(self):
        self._nota = sum(temporada.total_notas() for temporada in self.temporadas) / self.total_episodios()

# Métodos

    def adicionar_temporadas(self, numero):
        for i in range(1,numero+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.titulo} - Temporada {i}")
            temporada = Temporada(i)

            episodios = int(input(f"Quantidade de episódios: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.titulo} - Temporada {i}")
            self.temporadas.append(temporada)

            temporada.adicionar_episodios(episodios)

    def total_episodios(self):
        return sum(len(temporada) for temporada in self.temporadas)

        
# Métodos Especiaisdef duracao(self):

    def __len__(self):
        return len(self.temporadas)
    
    def __repr__(self):
        return f"Serie {self.titulo} ({len(self.temporadas)} temporadas)"