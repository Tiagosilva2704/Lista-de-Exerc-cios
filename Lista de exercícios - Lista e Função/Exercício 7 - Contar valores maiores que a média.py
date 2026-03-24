# Contar valores maiores que a média
def contar_acima_da_media(lista):
    media = sum(lista) / len(lista)
    return sum(1 for x in lista if x > media)

num = [1, 2, 3, 4, 5] # Média 3
print(num)
print(contar_acima_da_media(num))

### Se quiser somar os valores acima da média, '1' por 'x'.
# def contar_acima_da_media(lista):
#     media = sum(lista) / len(lista)
#     return sum(x for x in lista if x > media)

# num = [1, 2, 3, 4, 5] 
# print(num)
# print(contar_acima_da_media(num))