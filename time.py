#O código a seguir coleta as cotações das ações nos últimos meses.

from datetime import date, timedelta
import yfinance as yf
from datetime import datetime
import pandas

def gerar_historico():
    hoje = date.today()
    passado = hoje - timedelta(365)

    ativos = {"Ambev":"ABEV3.SA", "Bancodobrasil":"BBAS3.SA", "B3":"B3SA3.SA", "Cielo":"CIEL3.SA", "Eletrobras":"ELET3.SA", "Fleury":"FLRY3.SA", "Gol":"GOLL4.SA", "Jbs":"JBSS3.SA", "Mrv":"MRVE3.SA", "Petrobras":"PETR3.SA", "Vale":"VALE3.SA"}
    for companhia, codigo in ativos.items():
        nome = companhia
        x = yf.Ticker(codigo).history(start = passado, end = hoje, interval = "1mo")
        print(nome, ": \n", x, "\n")
        contador = -1
        lista = []
        tam = len(x.index)
        index = range(tam)
        x.index = index
        for linha in x.values:
            contador += 1    
            for celula in linha:
                if pandas.isna(celula) == True:
                    lista.append(contador)          
        x = pandas.DataFrame(data=x.drop(lista))
        companhia = x      
        print(nome, ": \n", companhia, "\n")

