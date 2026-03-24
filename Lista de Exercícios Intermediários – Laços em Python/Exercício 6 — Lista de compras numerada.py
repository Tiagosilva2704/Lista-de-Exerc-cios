# Dada a lista abaixo:

compras = ["arroz", "feijão", "macarrão", "leite", "pão"]
# Use enumerate() para exibir a lista no formato:

# 1 - arroz
# 2 - feijão
# 3 - macarrão
# 4 - leite
# 5 - pão

for i, p in enumerate(compras, start=1):
    print(f'{i} - {p}')