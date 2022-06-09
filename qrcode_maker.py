import qrcode
#Esse módulo é necessário para criar um qrcode e associar algo a ele.
carteira_1 = {}
carteira_2 = {}
carteira_3 = {}
#Essas carteiras são modelos para testar o programa.
valores_hoje = {}
#Esse dicionário aramzenará o valor de cada moeda e ação.
total_carteira = 0
#Essa variável receberá o valor da carteira analisada.

for tipo, quantidade in carteira_1:
    valor = valores_hoje[tipo]
    total_carteira = total_carteira + quantidade*valor
#Essa estrutura percorre a carteira_1, e soma ao total da carteira o valor de cada componente da carteira.
    
imagem_qrcode = qrcode.make(f"Você tem o equivalente a {total_carteira} reais.")
#Esse comando cria um qrcode associado à frase inserida como parÂMETRO.
imagem_qrcode.save("qrcode_python.png")
#Esse comando salva o qrcode como um arquivo png.
