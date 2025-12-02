class Midia:
    """
    Classe base para representar qualquer mídia (filme ou série).
    """
    def __init__(self, titulo, tipo, genero, ano, classificacao_indicativa, elenco, status):
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.classificacao_indicativa = classificacao_indicativa
        self.elenco = []
        self.status = status

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

 # Métodos
    
    def atualizar_status(self, status):
        lista_status = ["NÃO ASSISTIDO", "ASSISTINDO", "ASSISTIDO"]
        if status not in lista_status:
            print("Digite um status válido.")
        else:
            self.status = status

# Métodos Especiais

    def __str__(self):
        return f"{self.titulo} ({self.tipo}) - {self.ano}"

    def __eq__(self, outro):
        if not isinstance(outro, Midia):
            return NotImplemented
        return self.titulo == outro.titulo and self.tipo == outro.tipo and self.ano == outro.ano