# Dado o dicionário:

alunos = {
    "Ana": 8,
    "Carlos": 5,
    "Marina": 7,
    "João": 4
}
# Use for para:

# mostrar cada aluno e sua nota;
# informar se ele está Aprovado (nota >= 6) ou Reprovado.

for i, j in alunos.items():
    if j >= 6:
        print(f'{i} - Aprovado(a) - Nota: {j}')
    else:
        print(f'{i} - Reprovado(a) - Nota: {j}')