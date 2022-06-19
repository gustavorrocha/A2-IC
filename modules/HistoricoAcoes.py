import yahooquery as yq
from datetime import date, timedelta


def obter_dados(carteira):
    acoesemoedas = []
    for papeis in carteira: #pegar ações e moedas
        for acoesoumoeda in carteira[papeis]:
            acoesemoedas.append(acoesoumoeda["Nome"]) #lista com todos os nomes de ações e moedas
    return yq.Ticker(acoesemoedas)


def obter_currencies(carteira, dados):
    currencies = {}
    for acao in carteira["Ações"]:
        nomeacao = acao["Nome"]
        #procurar a moeda que essa ação está cotada
        currencies[nomeacao] = dados.price[nomeacao]["currency"]  + "BRL=X" #adicionando as currencies no dicionário
    return currencies


def obter_dados_currencies(carteira, dados):
    #conjunto para eliminar repetições
    currencies = obter_currencies(carteira, dados)
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
    return currencies


def obter_historico(dados, nome):
    hoje = date.today()
    passado = hoje - timedelta(365)
    print(dados.history(start = passado, end = hoje, interval = "1mo"))
    historico = dados.history(start = passado, end = hoje, interval = "1mo")
    historico_acao = historico["symbol"] == nome
    return historico_acao


def inserir_dados_dicionario(carteira):
    dados = obter_dados(carteira)
    currencies = obter_dados_currencies(carteira, dados)
    #dado da ação e multiplicar pela currency
    for papeis in carteira:
        for acoesoumoeda in carteira[papeis]:
            nome = acoesoumoeda["Nome"]
            if nome == "BRL=X":
                preco = 1
            else:
                preco = dados.price[nome]["regularMarketPrice"]
            if papeis == "Ações":
                preco *= currencies[nome]
            acoesoumoeda["Preço"] = round(preco,2) #arredondar o preço em duas casas decimais
            acoesoumoeda["Quantidade"] = float(acoesoumoeda["Quantidade"])
            precototal = preco * acoesoumoeda["Quantidade"]
            acoesoumoeda["Preço Total"] = round(precototal,2)
            #acoesoumoeda["Histórico"] = obter_historico(dados, nome)
    return carteira