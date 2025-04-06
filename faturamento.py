import json

def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]
    
    if not faturamento:
        print("Não há dados de faturamento válidos.")
        return
    
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    print(f"Menor faturamento diário: {menor_faturamento}")
    print(f"Maior faturamento diário: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")


processar_faturamento('C:/Users/User/Desktop/teste/dados.json')
