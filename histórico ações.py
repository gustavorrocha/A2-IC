import yfinance as yf
Ações_da_carteira = {"ambev", "bancodobrasil", "b3", "cielo", "eletrobras", "fleury" ,"gol", "jbs", "mrv", "petrobras", "vale"}

ambev = yf.Ticker("ABEV3.SA")
ambev_historical = ambev.history(start = "2020-01-01", end = "2022-05-30")
print("Ambev: \n", ambev_historical, "\n")

bancodobrasil = yf.Ticker("BBAS3.SA")
bancodobrasil_historical = bancodobrasil.history(start = "2020-01-01", end = "2022-05-30")
print("Banco do Brasil: \n", bancodobrasil_historical, "\n")

b3 = yf.Ticker("B3SA3.SA")
b3_historical = b3.history (start = "2020-01-01", end = "2022-05-30")
print("B3: \n", b3_historical, "\n")

cielo = yf.Ticker("CIEL3.SA")
cielo_historical = cielo.history (start = "2020-01-01", end = "2022-05-30")
print("Cielo: \n", cielo_historical, "\n")

eletrobras = yf.Ticker("ELET3.SA")
eletrobras_historical = eletrobras.history(start = "2020-01-01", end = "2022-05-30")
print("Eletrobras: \n", eletrobras_historical, "\n")

fleury = yf.Ticker("FLRY3.SA")
fleury_historical = fleury. history(start = "2020-01-01", end = "2022-05-30")
print("Fleury: \n", fleury_historical, "\n")

gol = yf.Ticker("GOLL4.SA")
gol_historical = gol.history(start = "2020-01-01", end = "2022-05-30")
print("Gol: \n", gol_historical, "\n")

jbs = yf.Ticker("JBSS3.SA")
jbs_historical = jbs.history(start = "2020-01-01", end = "2022-05-30")
print("JBS: \n", jbs_historical, "\n")

mrv = yf.Ticker("MRVE3.SA")
mrv_historical = mrv.history(start = "2020-01-01", end = "2022-05-30")
print("MRV: \n", mrv_historical, "\n")

petrobras =  yf.Ticker("PETR3.SA")
petrobras_historical = petrobras.history(start = "2020-01-01", end = "2022-05-30")
print ("Petrobras: \n", petrobras_historical, "\n")


vale = yf.Ticker("VALE3.SA")
vale_historical = vale.history (start = "2020-01-01", end = "2022-05-30")
print("Vale: \n", vale_historical, "\n")


