from midia import Midia

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao_indicativa, elenco, data_lancamento, status, temporada):
        super().__init__(titulo, "SERIE", genero, ano, duracao, classificacao_indicativa, elenco, data_lancamento, status)
        self.temporada = []

    # Encapsulamento

    @property
    def temporada(self):
        return self._temporada

    @temporada.setter
    def temporada(self, temporada):
        if temporada <= 0:
            print("Número de temporadas deve ser positivo.")
        else:
            self._temporada = temporada
            
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