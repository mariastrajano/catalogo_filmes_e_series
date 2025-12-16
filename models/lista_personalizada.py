import os

class ListaPersonalizada:
    """
    Representa uma lista personalizada de mídias.
    """
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar(self, midia):
        if midia not in self.midias:
            self.midias.append(midia)
            print("")
            print("Mídia adicionada com sucesso!")
            print("")

    def remover(self, midia):
        if midia in self.midias:
            self.midias.remove(midia)
            print("")
            print("Mídia removida com sucesso!")
            print("")

    def listar(self):
        print(f"=== {self.nome} ===")

        if not self.midias:
            print("Lista vazia.")
            print("")

        else:
            for i, midia in enumerate(self.midias, 1):
                print(f"{i}. {str(midia)}")
