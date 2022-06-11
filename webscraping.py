import requests
import lxml
from bs4 import BeautifulSoup

url = "https://almirfonseca.github.io/A2-IC/carteira_mariana.html"
response = requests.get(url)

page = BeautifulSoup(response.text, 'lxml')
dict = {}
for actions in page.select("div tr"):
    action = actions.select("td")
    if len(action) > 0:
        dict[actions.select("td")[0].text] = actions.select("td")[1].text

print(dict)
