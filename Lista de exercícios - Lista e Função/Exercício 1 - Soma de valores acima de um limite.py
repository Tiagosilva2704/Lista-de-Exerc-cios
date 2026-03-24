# Soma de valores acima de um limite
def soma_acima_limite(lista, limite):
    return sum(x for x in lista if x > limite)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
limite = int(input("Digite o limite: "))

print(soma_acima_limite(num, limite))