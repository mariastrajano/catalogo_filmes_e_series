class Midia:
    """
    Classe base para representar qualquer mídia (filme ou série).
    """
    def __init__(self, titulo, tipo, genero, ano, duracao, classificacao_indicativa, elenco, status, nota):
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
        self.classificacao_indicativa = classificacao_indicativa
        self.elenco = elenco
        self.status = status
        self.nota = nota
    
    def atualizar_status(self, novo_status):
        self.status = novo_status