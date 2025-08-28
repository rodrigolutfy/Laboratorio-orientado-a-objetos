class Produto:
    # Metodo Contrutor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def apresentacao(self):
        print(f"produto = {self.nome} | preco = {self.preco} | quantidade = {self.quantidade}")


leite = Produto("Leite", 7.99, 10)
maca = Produto("Maça", 0.99, 10)
agua = Produto("agua", 1.99, 20)


