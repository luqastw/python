# Importação de todos os módulos de array.
# from array import array

# Exemplo de recursividade.
def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

countdown(5) # 5 4 3 2 1 0

# Exemplo de custom module.
import lqsmath

soma = lqsmath.soma
soma(1, 2)

# Exemplo do uso de lambda.
somar = lambda x, y: x + y
somar(1, 4)