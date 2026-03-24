# 1.2.1 Maior de três números
# Leia três números e mostre o maior usando apenas condicionais (sem usar max).

num1 = int(input(' Digite o primeiro número: '))
num2 = int(input(' Digite o segundo número: '))
num3 = int(input(' Digite o terceiro número: '))
maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
     
print(f' O maior número é: {maior}')