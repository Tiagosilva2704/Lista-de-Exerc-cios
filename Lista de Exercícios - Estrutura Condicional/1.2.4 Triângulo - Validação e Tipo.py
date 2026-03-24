# 1.2.4 Triângulo: validação e tipo
# Leia três lados. Primeiro, verifique se formam um triângulo (cada lado < soma dos outros dois).
# Se sim, classifique:
# • Equilátero: três lados iguais
# • Isóscelesp: dois lados iguais
# • Escaleno: três lados diferentes

a = float(input('Informe o lado 1: '))
b = float(input('Informe o lado 2: '))
c = float(input('Informe o lado 3: '))     

if (a + c < b) or (a + b < c) or (b + c < a):
    print('Não é um triangulo.')
elif (a == b) and (a == c):
    print('Este é um triangulo Equilatero')
    # Se todos os lados são iguais, não passa para o proximo item.
    
elif (a == b) or (a == c) or (b == c):
    print('Este é um triangulo Isósceles')
    # Assim como foi checado no elif anterior, todos os lados não iguais, então testa se algum dos lados é igual ao outro. Se não ter nenhum, passa para o else a seguir.
    
else:
    print('Este é um triangulo Escaleno')