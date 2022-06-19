import qrcode
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
#Esse módulo é necessário para criar um qrcode e associar algo a ele.


#Função que calcula o valor de determinada carteira
def criar_qrcode(carteira):
    soma = 0 #Essa variável receberá o valor da carteira analisada.
    acoes = carteira["Ações"]
    for acao in acoes:
        soma = soma + acao["Preço Total"]
        #Essa estrutura percorre cada elemento da tupla armazenada em acoes. Esse elemento é um dicionário, do qual seleciona-se o valor correspondente à chave 'Preço (total)'. Esse valor é somado à variável soma.
    moedas = carteira["Moedas"]
    for moeda in moedas:
        soma = soma + moeda["Preço Total"]
        #Essa estrutura percorre cada elemento da tupla armazenada em moedas. Esse elemento é um dicionário, do qual seleciona-se o valor correspondente à chave 'Preço (total)'. Esse valor é somado à variável soma.
    gerar_qrcode(soma)


#Função que gera um qrcode
def gerar_qrcode(valor):
    imagem_qrcode = qrcode.make(f"Você tem o equivalente a {valor} reais.") #Esse comando cria um qrcode associado à frase inserida como parâmetro.
    imagem_qrcode.save("carteira.png") #Esse comando salva o qrcode como um arquivo png.
    anexar()

def anexar():
    wb = load_workbook(filename = "temp.xlsx")
    ws = wb.active
    img = Image("carteira.png") 
    img.height = 150
    img.width = 150 
    ws.add_image(img, "U15") # “U” representa a coluna e “15” representa a linha em que o canto superior esquerdo da imagem está localizado.
    wb.save(filename = "temp.xlsx") 