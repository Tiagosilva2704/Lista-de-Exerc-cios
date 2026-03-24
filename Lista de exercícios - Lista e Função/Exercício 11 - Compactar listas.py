# Compactar listas
def compactar(lista):
    resultado = []
    valor_atual = lista[0] # [0] passa pelo primeiro item, ja 'vendo' ele
    # tem que comecar com lista[0] se não vai contar a lista toda de uma vez, ao invez de só os elementos dentro dela.
    contagem = 1 # tem que comecar em 1 pq se não conta o primeiro item duas vezes

    # Percorremos a partir do segundo elemento
    for x in lista[1:]: # tem que ser [1:] se não o primeiro item vai ser contado duas vezes, por que o valor_atual já é o primeiro item da lista.
        if x == valor_atual:
            contagem += 1
        else:
            resultado.append((valor_atual, contagem))
            valor_atual = x
            contagem = 1

    resultado.append((valor_atual, contagem))  # adiciona o último grupo
    return resultado

lista = [1, 1, 2, 3, 3, 3, 4]
print(compactar(lista))
# resultado: [(1, 2), (2, 1), (3, 3), (4, 1)] o numero 1 repetiu duas vezes (1, 2)... o numero 3 repetiu 3 vezes (3, 3)...