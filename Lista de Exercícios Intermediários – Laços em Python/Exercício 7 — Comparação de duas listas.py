# Dadas as listas:

nomes = ["Ana", "Carlos", "João", "Marina"]
notas = [8.5, 6.0, 9.2, 7.1]
# Use zip() para mostrar:

# Ana tirou 8.5
# Carlos tirou 6.0
# João tirou 9.2
# Marina tirou 7.1

for n, no in zip(nomes, notas):
    print(f'{n} tirou {no}')