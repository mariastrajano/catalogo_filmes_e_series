import os
import datetime
from src.midia import Midia
from src.temporada import Temporada

import sqlite3
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

class Serie(Midia):
    """
    Representa uma série no catálogo.
    Herda comportamento e atributos da classe Midia.
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao):
        super().__init__(titulo, "SERIE", genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao)
        self.temporadas = []

# Encapsulamento

    def set_duracao(self):
        self._duracao = sum(temporada.duracao() for temporada in self.temporadas)

        cursor.execute("UPDATE midias SET duracao = '"+str(self._duracao)+"' WHERE titulo = '"+self.titulo+"'")
        banco.commit()

    def set_status(self):
        ep_assistidos = 0
        for temporada in self.temporadas:
            if temporada.episodios_assistidos() == True:
                ep_assistidos += 1
                
        if ep_assistidos == self.total_episodios():
            self._status = "ASSISTIDO"
            self._data_conclusao = datetime.date.today().isoformat()

            cursor.execute("UPDATE midias SET status = '"+self._status+"' WHERE titulo = '"+self.titulo+"'")
            cursor.execute("UPDATE midias SET data_conclusao = '"+self._data_conclusao+"' WHERE titulo = '"+self.titulo+"'")
            banco.commit()


    def set_nota(self):
        self._nota = sum(temporada.total_notas() for temporada in self.temporadas) / self.total_episodios()

        cursor.execute("UPDATE midias SET nota = '"+str(self._nota)+"' WHERE titulo = '"+self.titulo+"'")
        banco.commit()

# Métodos

    def adicionar_temporadas(self, numero):
        for i in range(1, numero+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.titulo} - Temporada {i}")
            temporada = Temporada(i)

            episodios = int(input(f"Quantidade de episódios: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.titulo} - Temporada {i}")
            self.temporadas.append(temporada)

            temporada.adicionar_episodios(episodios)

    def total_episodios(self):
        return sum(len(temporada) for temporada in self.temporadas)

        
# Métodos Especiaisdef duracao(self):

    def __len__(self):
        return len(self.temporadas)
    
    def __repr__(self):
        return f"Serie {self.titulo} ({len(self.temporadas)} temporadas)"
