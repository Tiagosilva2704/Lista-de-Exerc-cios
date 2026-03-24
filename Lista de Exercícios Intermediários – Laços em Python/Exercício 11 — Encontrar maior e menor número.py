# Peça 5 números ao usuário.

# Utilizando laço, determine:

# o maior número;
# o menor número.
# Regra: não use max() nem min(). Faça a comparação manualmente com laço e condicionais.

n1 = int(input(' Digite um numero: '))
n2 = int(input(' Digite um numero: '))
n3 = int(input(' Digite um numero: '))
n4 = int(input(' Digite um numero: '))
n5 = int(input(' Digite um numero: '))
numeros = [n1, n2, n3, n4, n5]
maior = n1
for i in numeros:
    if i > maior:
        maior = i
print(f' O maior número é: {maior}')