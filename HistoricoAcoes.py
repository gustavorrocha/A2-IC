import yfinance as yf
import yahooquery as yq

carteira = {"Ações": [{"Nome": "GOOGL", "Quantidade": 2},{"Nome": "AMZN", "Quantidade": 1}, {"Nome": "AAPL", "Quantidade": 5}, 
                      {"Nome": "PETR4.SA", "Quantidade": 10}, {"Nome": "VALE", "Quantidade": 15}], 
           "Moedas": [{"Nome": "USDBRL=X", "Quantidade": 150}, {"Nome": "BRL=X", "Quantidade": 200}, {"Nome": "EURBRL=X", "Quantidade": 100}]}

acoesemoedas = []
for papeis in carteira: #pegar ações e moedas
   for acoesoumoeda in carteira[papeis]:
       acoesemoedas.append(acoesoumoeda["Nome"]) #lista com todos os nomes de ações e moedas
dados = yq.Ticker(acoesemoedas).price

print(dados)
currencies = {}
for acao in carteira["Ações"]:
    nomeacao = acao["Nome"]
    #procurar a moeda que essa ação está cotada
    currencies[nomeacao] = dados[nomeacao]["currency"]  + "BRL=X" #adicionando as currencies no dicionário
    
    
#conjunto para eliminar repetições
currenciesunica = set(currencies.values())
print(currenciesunica)

#obter dados das currencies
dadoscurrency = yq.Ticker(currenciesunica)
print(dadoscurrency.price)

#dado da ação e multiplicar pela currency
for papeis in carteira:
    for acoesoumoeda in carteira[papeis]:
        nome = acoesoumoeda["Nome"]
        preco = dados[nome]["regularMarketPrice"]
        print(preco)
