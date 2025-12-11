class Episodio:
    """
    Representa um episódio de uma temporada.
    """
    def __init__(self, numero, titulo, duracao, status, nota):
        self.numero = numero
        self.titulo = titulo
        self.duracao = duracao
        self.status = status
        self.nota = nota

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in ["Não assistido", "Assistindo", "Assistido"]:
            raise ValueError("Status inválido!")
        else:
            self._status = status

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

# Métodos Especiais

    def __str__(self):
        return f"Ep {self.numero}: {self.titulo} ({self.duracao} min)"