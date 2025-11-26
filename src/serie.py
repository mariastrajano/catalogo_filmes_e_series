from src.midia import Midia

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, classificacao_indicativa, elenco, status, temporadas):
        super().__init__(titulo, "SERIE", genero, ano, classificacao_indicativa, elenco, status)
        self.temporadas = temporadas

    # Encapsulamento

    @property
    def temporadas(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, temporadas):
        if temporadas <= 0:
            raise ValueError("Número de temporadas deve ser positivo.")
        else:
            self._temporadas = temporadas

    # Métodos (ainda não implementados pois precisam da classe Temporada para funcionar)

    def adicionar_temporada():
        pass

    def total_episodios():
        pass

    def episodios_assistidos():
        pass

    def atualizar_status():
        pass

    def media_nota():
        pass