# 1.1.3 Desconto simples
# Leia o valor de uma compra. Se for maior que 100, aplique 10% de desconto; caso contrário,
# 5%. Mostre o valor final.

valor = float(input('Digite o valor da compra: '))

if valor >= 100:
    valor -= valor*0.1
    print(f' Novo valor com desconto aplicado: R${valor:.2f}')
else:
    print(f' O valor não recebe desconto')