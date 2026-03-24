# 1.1.5 Ano bissexto
# Peça um ano e informe se é bissexto. Regras:
# • É bissexto se é divisível por 4 e não é divisível por 100;
# • Ou se é divisível por 400.

ano = int(input('Digite o ano: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f' O ano {ano} é bissexto.')
else:
    print(f' O ano {ano} não é bissexto.')