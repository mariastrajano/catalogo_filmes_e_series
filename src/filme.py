from midia import Midia

class Filme(Midia):
    """
    Representa um filme no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao_indicativa, elenco, data_lancamento, status, nota):
        super().__init__(titulo, "FILME", genero, ano, duracao, classificacao_indicativa, elenco, data_lancamento, status)
        self.nota = nota

# Encapsulamento

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            print("A nota deve ser entre 0 e 10.")
        else:
            self._nota = nota