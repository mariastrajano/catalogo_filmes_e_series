from src.midia import Midia

class Filme(Midia):
    """
    Representa um filme no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, classificacao_indicativa, elenco, status, duracao, nota):
        super().__init__(titulo, "FILME", genero, ano, classificacao_indicativa, elenco, status)
        self.duracao = duracao
        self.nota = nota

# Encapsulamento

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve ser entre 0 e 10.")
        else:
            self._nota = nota

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        if duracao <= 0:
            raise ValueError("Duração deve ser maior que zero.")
        else:
            self._duracao = duracao