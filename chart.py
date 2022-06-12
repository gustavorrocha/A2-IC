#Nesse arquivo serão gerados gráficos a partir dos dados das carteiras.

from openpyxl import load_workbook #Essa função será necessária para carregar o workbook gerado anteriormente (no branch DadosExcel).
from openpyxl.chart import BarChart, Series, Reference #Essas funções são necessárias para construir os gráficos.

wb = load_workbook(filename = 'teste189.xlsx') #Carrega o arquivo em excel.
ws = wb.active #Grava a planilha ativa.
ws_2 = wb.create_sheet() #Cria uma nova planilha.

#O código a seguir é o esqueleto de um gráfico.
chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "Valor dos ativos"
chart1.y_axis.title = "mm"
chart1.x_axis.title = "nn"

data = Reference(ws, min_col=3, min_row=3, max_row=7, max_col=3)
cats = Reference(ws, min_col=1, min_row=2, max_row=7)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
chart1.shape = 4
ws.add_chart(chart1, "A10")

#Uma cópia do arquivo com as modificações feitas é criada.
wb.save("bar.xlsx")

