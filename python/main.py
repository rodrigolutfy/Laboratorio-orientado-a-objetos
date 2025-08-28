from produto import Produto as prod
from gestao_escola import Escola as scho


produto1 = prod("Leite", 20.00, 40)
produto2 = prod("Maca", 30.00, 40)
produto3 = prod("agua", 50.00, 30)

aluno1 = scho("rodrigo", 21)
aluno2 = scho("joao", 20)
aluno3 = scho("caio", 22)

lista1 = [produto1, produto2, produto3]
lista2 = [aluno1, aluno2, aluno3]

for i in range(3):
    lista2[i].apresentacao(), print("comprou"), lista1[i].apresentacao() 