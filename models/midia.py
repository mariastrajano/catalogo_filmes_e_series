class Midia:
    """
    Classe base para Filme e Série.
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

    # -------------------
    # ENCAPSULAMENTO
    # -------------------

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
        if duracao < 0:
            raise ValueError("Duração deve ser maior que zero.")
        else:
            self._duracao = duracao

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
      
    # -------------------
    # MÉTODOS ESPECIAIS
    # -------------------

    def __str__(self):
        return f"{self.titulo} ({self.tipo}) - {self.ano} \n   Status: {self.status} \n   Nota: {self.nota}"

    def __eq__(self, outro):
        if not isinstance(outro, Midia):
            return NotImplemented
        
        return (self.titulo == outro.titulo and
                self.tipo == outro.tipo and
                self.ano == outro.ano)