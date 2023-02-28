# Define um dicionário com o faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total mensal da distribuidora
total_mensal = sum(faturamento_mensal.values())

# Calcula o percentual de representação de cada estado
percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_mensal.items()}

# Imprime os resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")