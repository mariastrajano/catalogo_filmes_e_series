from src.episodio import Episodio

class Temporada:
    """
    Representa uma temporada de uma série.
    """
    def __init__(self, numero):
        self.numero = numero
        self.episodios = []

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
    
# Métodos

    def adicionar_episodios(self, numero):
        
        for i in range(1,numero+1):
            print(f"EPISÓDIO {i}")
            titulo = input("Título: ").upper()
            duracao = int(input("Duração (em mim): "))
            status = input("Status: ").upper()
            nota = float(input("Nota: "))
            print("--------------")

            episodio = Episodio(i, titulo, duracao, status, nota)
            self.episodios.append(episodio)
    
    def listar_episodios(self):
        print(f"Temporada {self.numero}")
        for episodio in self.episodios:
            print(str(episodio))
    
    def media_notas(self):
        return sum(episodio.nota for episodio in self.episodios) / len(self)

# Métodos Especiais

    def __len__(self):
        return len(self.episodios)