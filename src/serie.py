from src.midia import Midia
from src.temporada import Temporada

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, classificacao, elenco, status):
        super().__init__(titulo, "SERIE", genero, ano, classificacao, elenco, status)
        self.temporadas = []

# Métodos

    def adicionar_temporadas(self, numero):
        temporada = Temporada(numero)
        self.temporadas.append(temporada)

    def total_episodios(self):
        return sum(len(temporada) for temporada in self.temporadas)

    def episodios_assistidos():
        pass

    def atualizar_status():
        pass

    def media_nota():
        pass

# Métodos Especiais

    def __len__(self):
        return len(self.temporadas)
    
    def __repr__(self):
        return f"Serie {self.titulo} ({len(self.temporadas)} temporadas)"