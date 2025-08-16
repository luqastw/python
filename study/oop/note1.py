# Revisão de sintaxe e funcionalidade de classes/objetos em Python.

class testClass:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    

res = testClass("lucas", 19, "M")
print(res.nome, res.idade, res.sexo)