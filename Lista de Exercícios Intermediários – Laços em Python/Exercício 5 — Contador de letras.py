# Peça uma palavra ao usuário.

# Utilizando for, conte:

# quantas vogais a palavra possui;
# quantas consoantes a palavra possui.
# Exemplo

# Entrada: engenharia

# Vogais: 5
# Consoantes: 6 (B, C, D..)

pal = input(' Digite uma palavra: ').lower()
vogais = ['a','e','i','o','u']
vogal = 0
consoante = 0
for i in (pal):
    if i not in vogais:
        consoante += 1
    else:
        vogal += 1
print(
    f'Vogais = {vogal}',
    f'Consoantes = {consoante}'
)