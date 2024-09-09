
valor_vendas = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_vendas = sum(valor_vendas.values())

porcentagens = {}
for estado, valor in valor_vendas.items():
    porcentagem = (valor / total_vendas) * 100
    porcentagens[estado] = round(porcentagem, 2)

print("Representação de cada estado por percentual: ")
for estado, porcentagem in porcentagens.items():
    print(f"{estado}: {porcentagem}%")