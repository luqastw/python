# Importação de todos os módulos de array.`1`
# from array import array

# Exemplo de recursividade.
def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

countdown(5) # 5 4 3 2 1 0

# Exemplo do uso de lambda.
soma_lambda = lambda x, y: x + y
print(soma_lambda(3, 4))