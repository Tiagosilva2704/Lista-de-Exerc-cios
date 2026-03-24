# Peça ao usuário um número maior que zero.

# Se ele digitar um valor inválido, peça novamente.

# Depois faça uma contagem regressiva até 0 usando while.

# Exemplo

# Digite um número: 5

# 5
# 4
# 3
# 2
# 1
# 0

while True:
    num = int(input(' Digite um número maior que 0: '))
    if num <= 0:
        print('Número inválido.')
        continue
    else:
        for i in range(num, -1, -1):
            print(i)
        break