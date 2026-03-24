# Crie um programa onde:

# o número secreto é 7;
# o usuário tenta adivinhar usando while.
# O programa deve informar:

# "Muito alto", quando o valor digitado for maior que 7;
# "Muito baixo", quando o valor digitado for menor que 7.
# Quando acertar, mostre:

# Parabéns! Você acertou!
# Tentativas: X

secreto = 7
tentativas = 0
while True:
    num = int(input(' Tente adivinhar o número: '))
    if num == secreto:
        print(
            ' Parabéns! Você acertou!',
            f'Tentativas: {tentativas}'
        )
    elif num > secreto:
        print('Muito alto!')
        tentativas += 1
        continue
    elif num < secreto:
        print('Multo Baixo!')
        tentativas += 1
        continue