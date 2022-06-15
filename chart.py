#Nesse arquivo serão gerados gráficos a partir dos dados das carteiras.

from openpyxl import load_workbook #Essa função será necessária para carregar o workbook gerado anteriormente (no branch DadosExcel).
from openpyxl.chart import BarChart, Series, Reference #Essas funções são necessárias para construir os gráficos.

wb = load_workbook(filename = 'teste189.xlsx') #Carrega o arquivo em excel.
ws = wb.active #Grava a planilha ativa.
ws_2 = wb.create_sheet() #Cria uma nova planilha.

#A seguir, iremos retirar das tabelas a informação a ser usada no gráfico e condensá-la na ws_2.
tipos = ()
valores = () #Essas tuplas armazenarão os tipos de ativo e seus valores.

#Com a estrutura a seguir, nós iteramos as linhas de interesse e a concatenamos à tupla correspondente.
for cell in ws.iter_rows(min_row=3,max_row=3,min_col=3,max_col=7,values_only=True):
    tipos = tipos + cell
for cell in ws.iter_rows(min_row=10,max_row=10,min_col=3,max_col=5,values_only=True):
    tipos = tipos + cell
for cell in ws.iter_rows(min_row=5,max_row=5,min_col=3,max_col=7,values_only=True):
    valores = valores + cell
for cell in ws.iter_rows(min_row=13,max_row=13,min_col=3,max_col=5,values_only=True):
    valores = valores + cell
#Com os comandos a seguir, as tuplas são alocadas em linhas da folha ws_2. Essas linhas serão usadas como referência no nosso gráfico.
ws_2.append(tipos)
ws_2.append(valores)

#O código a seguir é o esqueleto de um gráfico.
chart2 = BarChart()
chart2.type = "col"
chart2.style = 10
chart2.title = "Valor dos ativos"
chart2.y_axis.title = "Preço Total"
chart2.x_axis.title = "Ativos"

data = Reference(ws_2, min_col=1, min_row=1, max_row=2, max_col=8)
cats = Reference(ws_2, min_col=1, min_row=2, max_row=2, max_col=8)
chart2.add_data(data, titles_from_data=True)
chart2.set_categories(cats)
chart2.shape = 4
ws.add_chart(chart2, "I2")

#Uma cópia do arquivo com as modificações feitas é criada.
wb.save("bar.xlsx")

