# Exercício 1 — Soma de números digitados
# Crie um programa que peça números ao usuário continuamente.

# O programa deve:

# somar todos os números digitados;
# parar quando o usuário digitar 0.
# No final, mostre:
# a soma total;
# quantos números foram digitados (sem contar o 0).

# Exemplo
# Digite um número: 5
# Digite um número: 3
# Digite um número: 8
# Digite um número: 0
# Soma: 16
# Quantidade: 3

num = 0
qnt = 0

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        print(
            f'Soma = {num}',
            f'Qunatidade: {qnt}'
        )
        break
    else:
        num += n
        qnt += 1
        continue