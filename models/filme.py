from models.midia import Midia

class Filme(Midia):
    """
    Representa um filme no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao):
        super().__init__(titulo, "Filme", genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao)