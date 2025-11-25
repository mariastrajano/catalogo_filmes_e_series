class Episodio:
    """
    Representa um episódio de uma temporada.
    """
    def __init__(self, numero, titulo, duracao, status, nota):
        self.numero = numero
        self.titulo = titulo
        self.duracao = duracao
        self.status = "NÃO ASSISTIDO"
        self.nota = None

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

# Métodos
 
    def atualizar_status(self, status):
        lista_status = ["NÃO ASSISTIDO", "ASSISTINDO", "ASSISTIDO"]
        if status not in lista_status:
            print("Digite um status válido.")
        else:
            self.status = status