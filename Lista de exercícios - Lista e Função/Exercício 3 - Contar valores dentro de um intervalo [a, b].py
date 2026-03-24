# Contar valores dentro de um intervalo [a, b]
def contar_no_intervalo(lista, a, b):
    return sum(1 for x in lista if a <= x <= b)
# '1 for x in lista if a <= x <= b' faz que sempre que for possivel gerar um valor, ele vai 'retornar' 1, e ao final, vai somar todos e printar quantos numeros tem entre o intervalo.
num = [-2, -1, 0, 1, 2, 3]
print(num)
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

print(contar_no_intervalo(num, a, b))


### Se querer somar os valores dentro do intervalo, só precisa trocar o '1' por 'x'.
# def contar_no_intervalo(lista, a, b):
#     return sum(x for x in lista if a <= x <= b)
# num = [-2, -1, 0, 1, 2, 3]
# print(num)
# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))

# print(contar_no_intervalo(num, a, b))