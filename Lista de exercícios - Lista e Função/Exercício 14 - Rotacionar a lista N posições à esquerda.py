# Rotacionar a lista N posições à esquerda
def rotacionar(lista, n):
    # isso aqui faz com que nao tenha rotacoes sem precisar, por exemplo, se rotacionar uma lista de 5, 6 vezes é o mesmo que rotaconar só uma vez. Esse n = n % len(lista) faz com que só rotacione só o que precisar - não precisa para funcionar mas achei legal por.
    n = n % len(lista) 

    # Fatiamento: pega do índice n até o fim e junta com o início
    return lista[n:] + lista[:n]

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
n = int(input("Digite o número de posições para rotacionar: "))
print(rotacionar(lista, n))

# Se querer que rotacione para a direita, só precisa trocar o n por -n:
# def rotacionar(lista, n):
#     n = n % len(lista) 
#     return lista[-n:] + lista[:-n]

# lista = [1, 2, 3, 4, 5]
# print("Lista original:", lista)
# n = int(input("Digite o número de posições para rotacionar: "))
# print(rotacionar(lista, n))
