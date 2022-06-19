from modules import WebScraping
from modules import HistoricoAcoes
from modules import DadosExcel
from modules import QrcodeMaker
from modules import Chart


# Recebe como entrada a url da carteira a ser analisada
url = input("Digite a url da carteira: ")

print("Aguarde enquanto analisamos a sua carteira...\n")

# Monta a carteira a partir do scrapping da página da carteira
carteira = WebScraping.webscraping(url)

# Complementa a carteira com dados obtidos a partir do Yahoo Finance
dados_carteira = HistoricoAcoes.inserir_dados_dicionario(carteira)

# Gera um arquivo Excel com os resultados da análise
DadosExcel.criar_excel(dados_carteira)

# Insere o QrCode no Excel
QrcodeMaker.criar_qrcode(carteira)

# Cria os gráficos no Excel
Chart.criar_graficos(carteira)