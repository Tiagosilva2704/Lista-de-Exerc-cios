# Encontrar o segundo maior valor sem usar sort()
def segundo_maior(lista):
    maior = segundo = float('-inf') # tem que colocar esse -inf se não da erro, pq vai estar comparando o TIPO float ao invez de um valor.

    for x in lista:
        if x > maior:
            segundo = maior  # o antigo maior vira segundo
            maior = x # agora o maior é o x
        elif x > segundo and x != maior:
            segundo = x

    return segundo

num = [3, 1, 4, 1, 5, 9]
print(num)
print(segundo_maior(num))