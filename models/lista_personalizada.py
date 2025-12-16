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

            print(f"=== {self.nome} ===")
            print("Mídia adicionada com sucesso!")
            print("")

        else:
            print(f"=== {self.nome} ===")
            print("Mídia já faz parte da lista!")
            print("")

    def remover(self, midia):
        if midia in self.midias:
            self.midias.remove(midia)
    
            print(f"=== {self.nome} ===")
            print("Mídia removida com sucesso!")
            print("")

        else:
            print(f"=== {self.nome} ===")
            print("Mídia não faz parte da lista!")
            print("")

    def listar(self):
        print(f"=== {self.nome} ===")

        if not self.midias:
            print("Lista vazia.")

        else:
            for i, midia in enumerate(self.midias, 1):
                print(f"{i}. {str(midia)}")
        
        print("")
