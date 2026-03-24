# Multiplicar todos os elementos por um número
def multiplicar_elementos(lista, numero):
    return [x * numero for x in lista]
# 'X * numero' vai multiplicar cada elemento no for.
num = [1, 2, 3, 4, 5]
print(num)
numero = int(input("Digite um número para multiplicar os elementos da lista: "))

print(multiplicar_elementos(num, numero))