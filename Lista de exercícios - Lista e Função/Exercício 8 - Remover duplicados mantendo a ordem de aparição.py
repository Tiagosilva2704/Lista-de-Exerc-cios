# Remover duplicados mantendo a ordem de aparição
def remover_duplicados(lista):
    vistos = set()   # set faz com que não tenha repetidos, e cria um conjunto vazio.
    resultado = []
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado

lista = [1, 2, 3, 2, 4, 1, 5, 1, 5, 3, 4]
print(remover_duplicados(lista))