from models.episodio import Episodio

class Temporada:
    """
    Representa uma temporada de uma série.
    """
    def __init__(self, numero):
        self.numero = numero
        self.episodios = []

    # -------------------
    # ENCAPSULAMENTO
    # -------------------

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if numero <= 0:
            raise ValueError("Número de temporadas deve ser positivo.")
        else:
            self._numero = numero
    
    # -------------------
    # MÉTODOS
    # -------------------

    def adicionar_episodios(self, numero):
        
        for i in range(1,numero+1):
            print("-" * 10)
            print(f"EPISÓDIO {i}")
            titulo = input("Título: ").capitalize()
            duracao = int(input("Duração (em mim): "))
            status = input("Status (Não Assistido, Assistindo ou Assistido): ").capitalize()
            
            if status == "Assistido":
                nota = float(input("Nota (0-10): "))
            else:
                nota = 0.0

            episodio = Episodio(i, titulo, duracao, status, nota)
            self.episodios.append(episodio)
    
    def total_notas(self):
        return sum(episodio.nota for episodio in self.episodios)
    
    def episodios_assistidos(self):
            return len([episodio for episodio in self.episodios if episodio.status == "Assistido"])
                
    def duracao(self):
        return sum(episodio.duracao for episodio in self.episodios)

    # -------------------
    # MÉTODOS ESPECIAIS
    # -------------------

    def __len__(self):
        return len(self.episodios)