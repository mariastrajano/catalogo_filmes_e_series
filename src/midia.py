import datetime

import sqlite3
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

class Midia:
    """
    Classe base para representar qualquer mídia (filme ou série).
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota, data_conclusao):
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
        self.classificacao = classificacao
        self.elenco = elenco
        self.status = status
        self.nota = nota
        self.data_conclusao = data_conclusao

# Encapsulamento

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if titulo == "":
            raise ValueError("Título não pode ser vazio.")
        else:
            self._titulo = titulo

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        if duracao <= 0:
            raise ValueError("Duração deve ser maior que zero.")
        else:
            self._duracao = duracao

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in ["NÃO ASSISTIDO", "ASSISTINDO", "ASSISTIDO"]:
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
    def data_conclusao(self):
        return self._data_conclusao

    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
        if self._status == "ASSISTIDO":
            self._data_conclusao = datetime.date.today().isoformat()

            cursor.execute("UPDATE midias SET data_conclusao = '"+self._data_conclusao+"' WHERE titulo = '"+self.titulo+"'")
            banco.commit()

        else:
            self._data_conclusao = None

# Métodos

    def banco_de_dados(self):
        cursor.execute("INSERT INTO midias VALUES ('"+self.titulo+"', '"+self.tipo+"', '"+self.genero+"', '"+str(self.ano)+"', '"+str(self.duracao)+"', '"+str(self.classificacao)+"', '"+self.elenco+"', '"+self.status+"', '"+str(self.nota)+"', '"+str(self.data_conclusao)+"')")
        banco.commit()
        
# Métodos Especiais

    def __str__(self):
        return f"{self.titulo} ({self.tipo}) - {self.ano}"

    def __eq__(self, outro):
        if not isinstance(outro, Midia):
            return NotImplemented
        return self.titulo == outro.titulo and self.tipo == outro.tipo and self.ano == outro.ano