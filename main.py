# Importa as bibliotecas que seram utilizadas no código.
from random import random
import yfinance
from openpyxl import Workbook
from random import randrange

# ------------------------------------------------------------- #
# "Rascunho" para criar uma carteira em um modelo específico:
# ------------------------------------------------------------- #

usd = yfinance.Ticker("BRL=X") # Obtém os dados do "ticket" do dólar, com relação ao real.
try:
    usd_para_brl = usd.info["regularMarketPrice"] # Seleciona o valor atual do dólar.
except:
    print("ERRO") # Caso não haja conexão com o servidor, sai do programa e imprime uma mensagem de erro. 
    exit()


# Função que converte um dado preço em dólar, para real.
def converter_brl(preco_usd):
    preco_brl = preco_usd * usd_para_brl # Multiplica o preço em dólar com o valor do dólar, em real.
    return preco_brl


# Função que retorna o preço de um determinado ativo.
def preco_ativo(ativo):
    ticker = yfinance.Ticker(ativo) # Obtém os dados do "ticket" do ativo.
    preco_ativo_usd = float(ticker.info["regularMarketPrice"]) # Seleciona o valor atual do ativo.
    preco_ativo_brl = round(converter_brl(preco_ativo_usd), 2) # Converte o preço do ativo de dólar para real
    return preco_ativo_brl


# Função que completa um dicionário da carteira, com os dados de cada ativo e o seu valor total na carteira.
def completar_carteira(carteira, tipo):
    for ativo in carteira: # Inicia um loop com cada nome de ativo na carteira.
        nome = ativo["Nome"] # Obtém a lista com os dados de cada ativo.
        if tipo == "Moedas": # Formata o nome dos tipos de moeda para ser utilizada na biblioteca.
            nome += "USD=X"
        preco = preco_ativo(nome) # Encontra o preço do ativo.
        ativo["Preço (unitário)"] = preco # Adiciona o preço do ativo na lista de dados.
        ativo["Preço (total)"] = round(preco * ativo["Quantidade"], 2) # Adiciona o preço total do ativo nos dados. 


# Dicionário com apenas os nomes dos ativos e a quantidade presente na carteira.
carteira = {"Ações": [{"Nome": "GOOGL", "Quantidade": 2}, {"Nome": "AMZN", "Quantidade": 1}, {"Nome": "AAPL", "Quantidade": 5}, 
                      {"Nome": "PETR4.SA", "Quantidade": 10}, {"Nome": "VALE", "Quantidade": 15}], 
           "Moedas": [{"Nome": "USD", "Quantidade": 150}, {"Nome": "BRL", "Quantidade": 200}, {"Nome": "EUR", "Quantidade": 100}]}

# Utiliza a função feita para completar os dados da carteira
for tipo in carteira:
    completar_carteira(carteira[tipo], tipo)

# ------------------------------------------------------------- #
# Criação do arquivo Excel, com os dados da carteira:
# ------------------------------------------------------------- #

book = Workbook() # Inicia um workbook no Excel
sheet = book.active # Cria uma worksheet no workbook criado


# Função que insere os dados de uma lista em uma planilha, com cada elemento sendo inserido em uma linha diferente.
def inserir_dados(planilha, lista, linha_inicial, coluna):
    for linha, dado in enumerate(lista, linha_inicial):
        planilha.cell(row = linha, column = coluna).value = dado
    return linha # Retorna o número de linhas que foram inseridas pela função.


linha_tabela = 2 # Cria uma variável para armazenar a linha em que a inserção de dados começará.
coluna_tabela = 2 # Cria uma variável para armazenar a coluna em que a inserção de dados começará.

for tipo in carteira:
    sheet.cell(row = linha_tabela, column = coluna_tabela + 2).value = tipo # Insere o título do tipo de ativo na tabela.
    num_dados = inserir_dados(sheet, carteira[tipo][0], linha_tabela + 1, coluna_tabela) # Insere os títulos das linhas (utilizando o primeiro ativo do tipo).
    for num_ativo, ativo in enumerate(carteira[tipo], coluna_tabela + 2): # Loop que insere todos os dados de cada ativo na tabela.
        inserir_dados(sheet, ativo.values(), linha_tabela + 1, num_ativo)
    linha_tabela += num_dados + 1 # Altera a variável linha, para criar um espaço entre as tabelas de cada tipo.

nome_save = f"teste{str(randrange(1000))}.xlsx" # Gera um nome para o arquivo Excel.
book.save("./testes/" + nome_save) # Salva o arquivo na pasta de testes.
print(f"Arquivo {nome_save} criado") # Imprime o nome do arquivo criado.