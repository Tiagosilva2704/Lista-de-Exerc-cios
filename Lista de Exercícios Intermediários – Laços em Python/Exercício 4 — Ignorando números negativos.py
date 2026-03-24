# Exercício 4 — Ignorando números negativos
# Crie um programa que leia 8 números.

# Use continue para ignorar números negativos.

# No final, mostre a soma apenas dos números positivos.

num = 0
for i in range(1, 9):
    n = int(input(f'Digite o {i}° número inteiro: '))
    if n < 0:
        continue
    else:
        num += n
print(f'A soma dos positivos é: {num}')