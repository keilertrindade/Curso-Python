import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link').text
    data = pergunta.select_one('.relativetime').text
    voto = pergunta.select_one('.s-post-summary--stats-item-number').text

    print(titulo, data, " ", voto)
