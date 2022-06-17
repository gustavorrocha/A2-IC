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

    # Criando dicionários para receber os dados da carteira, especificando se é ação
    # ou moeda.
    carteira = {"Ações":[], "Moedas":[]}
    acoes = {}
    moedas = {}

    # Retirando os dados das ações e das moedas da carteira.
    for acao in pagina.select(".acao tr"):
        action = acao.select("td")
        if len(action) > 0:
            acoes[acao.select("td")[0].text] = acao.select("td")[1].text
    carteira["Ações"].append(acoes)
    for moeda in pagina.select(".moeda tr"):
        action = moeda.select("td")
        if len(action) > 0:
            moedas[moeda.select("td")[0].text] = moeda.select("td")[1].text
    carteira["Moedas"].append(moedas)
    return carteira
