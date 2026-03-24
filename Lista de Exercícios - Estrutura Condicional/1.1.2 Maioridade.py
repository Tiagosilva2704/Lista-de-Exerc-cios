# 1.1.2 Maioridade
# Leia a idade de uma pessoa e informe se é maior de idade (>= 18) ou menor de idade.

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f' Você é maior de idade. ({idade} anos)')
else:
    print(f' Voce é menor de idade. ({idade} anos)')