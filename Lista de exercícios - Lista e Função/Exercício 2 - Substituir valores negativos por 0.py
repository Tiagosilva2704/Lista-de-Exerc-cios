# Substituir valores negativos por 0
def substituir_negativos(lista):
    # max(0, x) compara qual é maior, 0 ou X. Retorna 0 se x for negativo, ou o próprio x se for maior que 0.
    return [max(0, x) for x in lista]

num = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

print(substituir_negativos(num))