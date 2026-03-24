# Verificar se um valor existe na lista
def valor_existe(lista, valor):
    return valor in lista  # quando usa in aqui ele retorna ou True ou False dependendo se o valor estiver na lista ou não

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = int(input("Digite um valor para verificar se existe na lista: "))
print(valor_existe(num, valor))