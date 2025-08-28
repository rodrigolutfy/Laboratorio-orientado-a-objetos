class Produto:
    # Metodo Contrutor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def apresentacao(self):
        print(f"produto = {self.nome} | preco = {self.preco} | quantidade = {self.quantidade}")