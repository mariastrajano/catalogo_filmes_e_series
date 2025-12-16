import os
import datetime
from models.midia import Midia
from models.temporada import Temporada

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao):
        super().__init__(titulo, "Serie", genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao)
        self.temporadas = []

    # -------------------
    # MÉTODOS
    # -------------------

    def adicionar_temporadas(self, numero):

        for i in range(1, numero+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- {self.titulo} - Temporada {i} ---")
            temporada = Temporada(i)

            episodios = int(input(f"Quantidade de episódios: "))
            
            self.temporadas.append(temporada)
            temporada.adicionar_episodios(episodios)

            self.status_automatico()
            self.duracao_total()
            self.nota_total()

    def total_episodios(self):
        return sum(len(temporada) for temporada in self.temporadas)
    
    def status_automatico(self):
        if sum(temporada.episodios_assistidos() for temporada in self.temporadas) == self.total_episodios():
            self.status = "Assistido"
            self.data_conclusao = datetime.date.today().isoformat()
        return self.status and self.data_conclusao

    def duracao_total(self):
        self.duracao = sum(temporada.duracao() for temporada in self.temporadas)
        return self.duracao
    
    def nota_total(self):
        self.nota = sum(temporada.total_notas() for temporada in self.temporadas) / self.total_episodios()
        return self.nota

        
    # -------------------
    # MÉTODOS ESPECIAIS
    # -------------------

    def __len__(self):
        return len(self.temporadas)
    
    def __repr__(self):
        return f"Serie {self.titulo} ({len(self)} temporadas)"