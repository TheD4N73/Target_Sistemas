import json

with open("dados.json") as file:
    data = json.load(file)

# Lista com os valores de faturamento diário
valores = [dado["valor"] for dado in data if dado["valor"] != 0]

# Menor e maior valor de faturamento diário
menor_valor = min(valores)
maior_valor = max(valores)

# Média mensal de faturamento (considerando apenas os dias com valor)
media_mensal = sum(valores) / len(valores)

# Número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = sum(valor > media_mensal for valor in valores)

print(f"Menor valor de faturamento diário: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
