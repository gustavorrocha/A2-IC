import qrcode
#Esse módulo é necessário para criar um qrcode e associar algo a ele.

soma = 0
#Essa variável receberá o valor da carteira analisada.

carteira = {'Ações': [{'Nome': 'GOOGL', 'Quantidade': 2, 'Preço (unitário)': 11451.03, 'Preço (total)': 22902.06}, {'Nome': 'AMZN', 'Quantidade': 1, 'Preço (unitário)': 592.02, 'Preço (total)':592.02}, {'Nome': 'AAPL', 'Quantidade': 5, 'Preço (unitário)': 722.86, 'Preço (total)': 3614.3}, {'Nome': 'PETR4.SA', 'Quantidade': 10, 'Preço (unitário)': 149.06, 'Preço (total)': 1490.6}, {'Nome': 'VALE', 'Quantidade': 15, 'Preço (unitário)': 87.4, 'Preço (total)': 1311.0}], 'Moedas': [{'Nome': 'USD', 'Quantidade': 150, 'Preço (unitário)': 4.89, 'Preço (total)': 733.5}, {'Nome': 'BRL', 'Quantidade': 200, 'Preço (unitário)': 1.0, 'Preço (total)': 200.0}, {'Nome': 'EUR', 'Quantidade': 100, 'Preço (unitário)': 5.24, 'Preço (total)': 524.0}]}
#Essa carteira é um modelo para testar o programa.

acoes = carteira['Ações']
for acao in acoes:
    soma = soma + acao['Preço (total)']
#Essa estrutura percorre cada elemento da tupla armazenada em acoes. Esse elemento é um dicionário, do qual seleciona-se o valor correspondente à chave 'Preço (total)'. Esse valor é somado à variável soma.
    
moedas = carteira['Moedas']
for moeda in moedas:
    soma = soma + moeda['Preço (total)']
#Essa estrutura percorre cada elemento da tupla armazenada em moedas. Esse elemento é um dicionário, do qual seleciona-se o valor correspondente à chave 'Preço (total)'. Esse valor é somado à variável soma.

imagem_qrcode = qrcode.make(f"Você tem o equivalente a {soma} reais.")
#Esse comando cria um qrcode associado à frase inserida como parâmetro.
imagem_qrcode.save("carteira.png")
#Esse comando salva o qrcode como um arquivo png.
