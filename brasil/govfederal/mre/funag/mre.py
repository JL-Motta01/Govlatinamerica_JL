from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests 

url = input("https://www.gov.br/mre/pt-br")
# teste (discursos: ministro das relações exteriores)
page = requests.get("https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/ministro-das-relacoes-exteriores")
soup = BeautifulSoup(page.content, 'html.parser')

# pegar todos os links da 'div titleContent'
lista_discursos_ministro = soup.find(class_='titleContent')
# pegar todos os conteudos da tag 'a' dentro da div 
lista_discursos_ministro_items = lista_discursos_ministro.find_all('a')
for discursos_ministro in lista_discursos_ministro:
    print(discrusos_ministro.prettify())
