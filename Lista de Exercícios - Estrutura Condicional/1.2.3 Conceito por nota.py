# 1.2.3 Conceito por nota
# Leia uma nota de 0 a 10 e mostre o conceito:
# • A: nota 9
# • B: 7 < nota < 9
# • C: 5 < nota < 7
# • D: 3 < nota < 5
# • E: nota < 3
# Valide a entrada: se a nota for fora do intervalo 0–10, mostre “nota inválida”.

while True:
        nota = float(input('Informe a nota: '))
        if nota > 10 or nota < 0:
            print('Digite um número dentre 0 e 10.')
            continue
        break

faixas = [
    (9, 'A'),
    (7, 'B'),
    (5, 'C'),
    (3, 'D'),
    (0, 'E')
]

for limite, conceito in faixas:
    # Limite é o o 9 em (9, 'A')
    if nota >= limite:
        print(f'O conceito para a nota {nota} é {conceito}.')
        break