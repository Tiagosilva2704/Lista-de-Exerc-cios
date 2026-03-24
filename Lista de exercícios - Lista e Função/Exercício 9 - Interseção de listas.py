# Interseção de listas (elementos em comum)
def intersecao(lista1, lista2):
    # set faz com que não tenha repetidos, assim da pra usar "&", que faz a interseção.
    # lembrar que & só funciona com sets.
    return list(set(lista1) & set(lista2))

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print(intersecao(lista1, lista2))