# Diferença entre listas (o que está na 1 mas não na 2)
def diferenca(lista1, lista2):
    # Quando se usa "-" em dois sets, ele retorna o que esta na primeira lista, mas não esta na segunda.
    return list(set(lista1) - set(lista2))

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(diferenca(lista1, lista2))
