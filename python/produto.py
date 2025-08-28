class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
leite = Produto("Leite", 7.99, 10)
maca = Produto("Maça", 0.99, 10)
agua = Produto("agua", 1.99, 20)
print(leite.preco, leite.nome,"quantidade:" {leite.quantidade})
