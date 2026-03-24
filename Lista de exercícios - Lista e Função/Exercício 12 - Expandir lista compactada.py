# Expandir lista compactada: [(valor, contagem)] → lista original
def expandir(lista_compactada):
    resultado = []
    for valor, contagem in lista_compactada:
        # extend adiciona vários elementos de uma lista de uma vez
        # [valor] * contagem cria uma lista com 'contagem' repetições
        resultado.extend([valor] * contagem) # (1 = valor, 2 = contagem)
    return resultado

resultado = [(1, 2), (2, 1), (3, 3), (4, 1)]
print(expandir(resultado))