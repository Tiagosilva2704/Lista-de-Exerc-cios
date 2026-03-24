# 1.2.2 IMC com faixas
# Leia peso (kg) e altura (m), calcule o IMC e classifique conforme as faixas:
# • Abaixo do peso: IMC < 18.5
# • Normal: 18.5 fi IMC < 25
# • Sobrepeso: 25 fi IMC < 30
# • Obesidade: IMC fi 30
# Fórmula: imc = peso / (altura ** 2)

kg = float(input('Informe o peso: '))
m = float(input('Informe a altura em cm: '))
m = m / 100
imc = kg / (m**2)

faixas = [
    (18.5, 'Abaixo do peso'),
    (25, 'Normal'),
    (30, 'Sobrepeso'),
    (float('inf'), 'Obesidade')
]

for limite, classificacao in faixas:
    if imc < limite:
        faixa = classificacao
        print(faixa)
        break