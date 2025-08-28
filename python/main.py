from produto import Produto as prod
produto1 = prod("Leite", 20.00, 40)
produto2 = prod("Maca", 30.00, 40)
produto3 = prod("agua", 50.00, 30)

for i in [produto1, produto2, produto3]:
    i.apresentacao()