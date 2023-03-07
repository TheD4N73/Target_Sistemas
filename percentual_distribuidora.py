faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_Outros = 19849.53

faturamento_total = faturamento_SP+faturamento_RJ+faturamento_MG+faturamento_ES+faturamento_Outros

percentual_sp = faturamento_SP / faturamento_total * 100
percentual_rj = faturamento_RJ / faturamento_total * 100
percentual_mg = faturamento_MG / faturamento_total * 100
percentual_es = faturamento_ES / faturamento_total * 100
percentual_outros = faturamento_Outros / faturamento_total * 100

print("Percentual:")
print(f"SP: {percentual_sp:.2f}%")
print(f"RJ: {percentual_rj:.2f}%")
print(f"MG: {percentual_mg:.2f}%")
print(f"ES: {percentual_es:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")
