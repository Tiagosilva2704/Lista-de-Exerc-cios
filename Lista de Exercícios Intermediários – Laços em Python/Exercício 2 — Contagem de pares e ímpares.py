# Peça 10 números ao usuário utilizando um for.

# Ao final, mostre:

# quantos números são pares;
# quantos números são ímpares.

pares = []
for i in range(10):
    i = int(input(' Digite um número: '))
    pares.append(i)
pares = [i for i in pares if i%2 == 0]
print(pares)