class Produto:
    # Metodo Contrutor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

leite = Produto("Leite", 7.99, 10)
maca = Produto("Maça", 0.99, 10)
agua = Produto("agua", 1.99, 20)

print(f"produto = {leite.nome} | preco = {leite.preco} | quantidade = {leite.quantidade}")
print(f"produto = {maca.nome} | preco = {maca.preco} | quantidade = {maca.quantidade}")
print(f"produto = {agua.nome} | preco = {agua.preco} | quantidade = {agua.quantidade}")
