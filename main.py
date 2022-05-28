# -------------------------------------------------------------------------------------- #
# "Rascunho" para criar uma carteira em um modelo específico:
# -------------------------------------------------------------------------------------- #

# Importa a biblioteca que será utilizada para adquirir informações sobre as ações.
import yfinance 


# Cria uma função que converte um dado preço em dólar, para real.
def converter_brl(preco_usd):
    usd = yfinance.Ticker("BRL=X") # Obtém os dados do "ticket" do dólar, com relação ao real.
    usd_para_brl = float(usd.history("today")["Close"]) # Seleciona o valor de fechamento do dólar.
    preco_brl = preco_usd * usd_para_brl # Multiplica o preço em dólar com o valor do dólar, em real.
    return preco_brl


# Cria uma função que retorna o preço de um determinado ativo.
def preco_ativo(ativo):
    ticker = yfinance.Ticker(ativo) # Obtém os dados do "ticket" do ativo. 
    preco_ativo_usd = float(ticker.history("today")["Close"]) # Seleciona o valor de fechamento do ativo.
    preco_ativo_brl = round(converter_brl(preco_ativo_usd), 2) # Converte o preço do ativo de dólar para real
    return preco_ativo_brl


# Cria uma função que completa um dicionário da carteira, com os dados de cada ativo e o seu valor total na carteira.
def completar_carteira(carteira, tipo):
    for nome in carteira: # Inicia um loop com cada nome de ativo na carteira.
        dados = carteira[nome] # Obtém a lista com os dados de cada ativo.
        if tipo == "Moeda": # Formata o nome dos tipos de moeda para ser utilizada na biblioteca.
            nome += "USD=X"
        preco = preco_ativo(nome) # Encontra o preço do ativo.
        dados.append(preco) # Adiciona o preço do ativo na lista de dados.
        dados.append(round(preco * dados[0], 2)) # Adiciona o preço total do ativo nos dados. 


# Cria um dicionário com apenas os nomes dos ativos e a quantidade presente na carteira,
carteira = {"Ações": {"GOOGL": [2], "AMZN": [1], "AAPL": [5], "PETR4.SA": [10], "VALE": [15]}, "Moedas": {"USD": [150], "BRL": [200], "EUR": [100]}}


# Utiliza a função feita para completar os dados da carteira
for tipo in carteira:
    completar_carteira(carteira[tipo], tipo)
