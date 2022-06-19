# Importando as bibliotecas a serem usadas.
import requests
import lxml
from bs4 import BeautifulSoup

# Criando a função para fazer o webscraping.
def webscraping(url):
    # Retirando o html da carteira.
    response = requests.get(url)
    # Facilitando a compreensão do html.
    pagina = BeautifulSoup(response.text, 'lxml')

    # Criando duas listas e um dicionário para receber os dados da carteira, especificando se é ação
    # ou moeda.
    carteira = {}
    acoes = []
    moedas = []

    # Retirando os dados das ações e das moedas da carteira.
    for acao in pagina.select(".acao tr"):  # Selecioando os tr's da classe acao no div para retirar somente as ações.
        ativo = acao.select("td")
        if len(ativo) > 0:
            dic_acoes = {}  # Criando um dicionário para receber as ações.
            dic_acoes["Nome"] = acao.select("td")[0].text  # Criando uma chave com o nome da ação.
            dic_acoes["Quantidade"] = acao.select("td")[1].text  # Criando uma chave com a quantidade de ações.
            acoes.append(dic_acoes)  # Adicionando as ações da carteira na lista de ações.
    carteira["Ações"] = acoes  # Adicionando a lista de ações no dicionário da carteira.

    for moeda in pagina.select(".moeda tr"):  # Selecioando os tr's dentro da classe moeda no div para retirar somente as moedas.
        ativo = moeda.select("td")
        if len(ativo) > 0:
            dic_moedas = {}  # Criando um dicionário para receber as moedas.
            dic_moedas["Nome"] = moeda.select("td")[0].text  # Criando uma chave com o nome da moeda.
            dic_moedas["Quantidade"] = moeda.select("td")[1].text  # Criando uma chave com a quantidade de dinheiro.
            moedas.append(dic_moedas)  # Adicionando as moedas da carteira na lista de moedas.
    carteira["Moedas"] = moedas  # Adicionando a lista de moedas no dicionário da carteira.

    return carteira