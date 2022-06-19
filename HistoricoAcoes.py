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

currencies = {}
for acao in carteira["Ações"]:
    nomeacao = acao["Nome"]
    #procurar a moeda que essa ação está cotada
    currencies[nomeacao] = dados[nomeacao]["currency"]  + "BRL=X" #adicionando as currencies no dicionário
    
    
#conjunto para eliminar repetições
currenciesunica = set(currencies.values())


#obter dados das currencies
dadoscurrency = yq.Ticker(currenciesunica).price
for acoes in currencies:
    moeda =  currencies[acoes]
    if moeda == "BRLBRL=X":
        valormoeda = 1
    else:
        valormoeda = dadoscurrency[moeda]["regularMarketPrice"]
    currencies[acoes] = valormoeda


#dado da ação e multiplicar pela currency
for papeis in carteira:
    for acoesoumoeda in carteira[papeis]:
        nome = acoesoumoeda["Nome"]
        if nome == "BRL=X":
            preco = 1
        else:
            preco = dados[nome]["regularMarketPrice"]
        if papeis == "Ações":
            preco *= currencies[nome]
        acoesoumoeda["Preço"] = round(preco,2) #arredondar o preço em duas casas decimais
        acoesoumoeda["Quantidade"] = float(acoesoumoeda["Quantidade"])
        precototal = preco * acoesoumoeda["Quantidade"]
        acoesoumoeda["Preço Total"] = round(precototal,2)

