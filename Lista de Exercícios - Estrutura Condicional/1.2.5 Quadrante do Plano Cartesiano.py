# 1.2.5 Quadrante do plano cartesiano
# Leia as coordenadas x e y de um ponto e indique em qual quadrante ele está:
# • Q1: x > 0 e y > 0
# • Q2: x < 0 e y > 0
# • Q3: x < 0 e y < 0
# • Q4: x > 0 e y < 0
# Se estiver sobre os eixos (x == 0 ou y == 0), informe “eixo”

x = float(input('Informe o valor de X: '))
y = float(input('Informe o valor de Y: '))

quadrantes = {
    'Q1': lambda x, y: x > 0 and y > 0,
    'Q2': lambda x, y: x < 0 and y > 0,
    'Q3': lambda x, y: x < 0 and y < 0,
    'Q4': lambda x, y: x > 0 and y < 0,
    'Eixo': lambda x, y: x == 0 or y == 0
}

for quadrante, funcao in quadrantes.items():
    # Quadrante são os (q1, q2, q3 e q4)
    # Funcao é a lambda
    if funcao(x, y): # Ta testando se os dois pontos retornam True no dicionario quando vão na lambda
        print(f' Os pontos {x} e {y} estão no quadrante {quadrante}')