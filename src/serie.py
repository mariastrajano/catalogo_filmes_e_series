import os
from src.midia import Midia
from src.temporada import Temporada

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, classificacao, elenco, status, nota):
        super().__init__(titulo, "SÉRIE", genero, ano, classificacao, elenco, status)
        self.nota = nota
        self.temporadas = []

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

    def status_automatico(self):
        for temporada in self.temporadas:
            if temporada.episodios_assistidos() == True:
                self.status == "ASSISTIDO"

    def media_notas(self):
        self.nota = sum(temporada.total_notas() for temporada in self.temporadas) / self.total_episodios()
    
# Métodos Especiais

    def __len__(self):
        return len(self.temporadas)
    
    def __repr__(self):
        return f"Serie {self.titulo} ({len(self.temporadas)} temporadas)"