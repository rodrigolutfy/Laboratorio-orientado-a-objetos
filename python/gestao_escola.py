class Escola:
    # Start da Classe POO
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota1 = None
        self.nota2 = None
        self.nota_final = None

    def apresentacao(self):
        print(f"aluno: {self.nome} idade: {self.idade}")
    
    def nota(self, nota_1, nota_2):
        self.nota1 = nota_1
        self.nota2 = nota_2
    
    def calcula(self):
        self.nota_final = (self.nota1+self.nota2)/2
        if self.nota_final >= 7:
            print(f"{self.nome} aprovado {self.nota_final}")
        elif self.nota_final >= 4 and self.nota_final < 7:
            print(f"{self.nome} recuperação {self.nota_final}")
        else:
            print(f"{self.nome} reprovado {self.nota_final}")













"""
ze = Escola("Zé da Manga", 18)

ze.nota(7,6)

print(f"Nome do aluno é: {ze.nome}")
print(f"Idade é: {ze.idade}")
print(f"Nota Prova 1 é: {ze.nota1}")
print(f"Nota Prova 2 é: {ze.nota2}")
ze.calcula()
"""