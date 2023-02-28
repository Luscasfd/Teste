import json

# Lê os dados de faturamento diário de um arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

# Remove os dias sem faturamento (finais de semana e feriados)
faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

# Calcula o menor e o maior valor de faturamento
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcula a média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum(valor > media_mensal for valor in faturamento_diario)

# Imprime os resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")