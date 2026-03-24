# Peça ao usuário um número inteiro.

# Mostre a tabuada de 1 a 10, mas interrompa a repetição com break quando o resultado da multiplicação ultrapassar 50.

# Exemplo

# Entrada: 7

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49

num = int(input('Digite um número inteiro: '))

for i in range(10):
    if num*i <= 50:
        print(f' {num} * {i} = {num * i}')
    else:
        break