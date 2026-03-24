# Usando for e range(), calcule a soma de todos os números de 1 a 100 que são múltiplos de 3.

# Mostre também:

# a soma total;
# quantos múltiplos de 3 existem nesse intervalo.

soma = 0
qnt = 0
for i in range(0, 100, 3):
    print(i)
    soma += i
    qnt += 1
    
print(
    f' Soma total: {soma}',
    f' Quantidade: {qnt}'
)