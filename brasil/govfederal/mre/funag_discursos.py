from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint


"""
# Realização de requisição de pagina web
# atraves da biblioteca urllib (requests)
"""
url = 'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores'
html = urlopen(url)

"""
# parseamento e extração das imformações da pagina web através do biblioteca BeautifulSoup

"""
bs = BeautifulSoup(html.read(), 'html.parser')

info_ministros = bs.find_all('p')

# pprint(info_ministros)

texto = []

for info_ministro in info_ministros:
    info_ministro = str(info_ministro)
    bsi = BeautifulSoup(info_ministro, "lxml")
    
    tmp=[]
    #extrai textos dos paragrafos
    for string in bsi.stripped_strings:
        palavras = repr(string)
        tmp.append(palavras)
     
    #extrai links dos paragrafos
    for link in bsi.find_all("a"):
        links = urllib.parse.urljoin(url,link['href'])
        tmp.append(links)
    texto.append(tmp)


texto2 = texto

#https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
#retira strings de lista de lista
#https://stackoverflow.com/questions/19220554/python-remove-elements-from-nested-lists
texto2 = [[i for i in texto if i != "'|'"] for texto in texto2]
#retira caracter de lista de lista
# https://stackoverflow.com/questions/31794610/removing-a-character-from-a-string-in-a-list-of-lists
texto2 = [[item.replace("'", "") for item in texto] for texto in texto2]

lista_ministros = texto2[4:-3]

# print(len(lista_ministros))

lista_ministro_bio = []
lista_ministro_discurso_posse = []
for ministro in lista_ministros:
    # discursos de posse + link do discurso para posse para bs
    if ministro[2] == 'Discurso de posse':
        lista_ministro_discurso_posse.append(ministro[-1])
    elif  ministro[2] != 'Discurso de posse':
        lista_ministro_discurso_posse.append("NA")
    
    if  ministro[2] != 'Discurso de posse':
        lista_ministro_bio.append(ministro[-1])
    elif  ministro[2] == 'Discurso de posse':
        lista_ministro_bio.append(ministro[-2])
  
# pprint(lista_ministro_bio)  
minstro_bio_paragrafo = []
for ministro_bio in lista_ministro_bio:
    # print(type(ministro_bio))
    url = ministro_bio
    html = urlopen(url)
    bsBio = BeautifulSoup(html.read(), 'html.parser')
    # pprint(bsBio)
    bio = bsBio.find_all('p')[-2]
    minstro_bio_paragrafo.append(bio.get_text())

ministro_discurso_posse_paragrafos = []
for ministro_discurso_posse in lista_ministro_discurso_posse[:2]:
    pprint(ministro_discurso_posse)
    url = ministro_discurso_posse
    html = urlopen(url)
    bsPosse = BeautifulSoup(html.read(), 'html.parser')
    tmp=[]
    #extrai textos dos paragrafos
    for string in bsPosse.stripped_strings:
        palavras = repr(string)
        tmp.append(palavras)
    pprint(tmp)
    
    
    
    
    

