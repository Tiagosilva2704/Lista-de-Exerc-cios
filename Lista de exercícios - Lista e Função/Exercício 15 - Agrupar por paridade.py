# Agrupar por paridade: pares primeiro, depois ímpares
def agrupar_paridade(lista):
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    return pares + impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(agrupar_paridade(lista))