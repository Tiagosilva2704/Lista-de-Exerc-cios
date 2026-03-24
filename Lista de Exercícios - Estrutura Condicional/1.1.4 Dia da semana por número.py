# 1.1.4 Dia da semana por número
# Leia um número inteiro de 1 a 7 e mostre o dia da semana correspondente:
# • 0 → domingo
# • 1 → segunda-feira
# • 2 → terça-feira
# • 3 → quarta-feira
# • 4 → quinta-feira
# • 5 → sexta-feira
# • 6 → sábado
# Se o número estiver fora desse intervalo, mostre “inválido”.


semana = {
    0: 'Domingo',
    1: 'Segunda-Feira',
    2: 'Terça-Feira',
    3: 'Quarta-Feira',
    4: 'Quinta-Feira',
    5: 'Sexta-Feira',
    6: 'Sábado'
}

while True:
    num = int(input('Digite o dia da semana em números (0-6): '))
    try:
        if num in semana:
            print(semana[num])
            break
        else:
            print('Não existe esse valor para dia de semana.')
            continue
    except TypeError:
        print('Digite apenas números inteiros.')
        continue            