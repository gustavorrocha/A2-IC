import yfinance as yf
ativos = {"Ambev":"ABEV3.SA", "Bancodobrasil":"BBAS3.SA", "B3":"B3SA3.SA", "Cielo":"CIEL3.SA", "Eletrobras":"ELET3.SA", "Fleury":"FLRY3.SA", "Gol":"GOLL4.SA", "Jbs":"JBSS3.SA", "Mrv":"MRVE3.SA", "Petrobras":"PETR3.SA", "Vale":"VALE3.SA"}
for companhia, codigo in ativos.items():
    nome = companhia
    companhia = yf.Ticker(codigo).history(start = passado, end = hoje, interval = "1mo")
    print(nome, ": \n", companhia, "\n")



    
    
    
