from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

##TODO
## Organizar o codigo em funções
## resolver bio com tag p vazias
## gerar html da bio e do discurso de posse

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

info_ministros = bs.find_all('p')  # ['p1','p2','p3'...]

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
texto2 = [[i for i in texto if i != "'-'"] for texto in texto2]
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
    elif ministro[2] != 'Discurso de posse':
        lista_ministro_discurso_posse.append("NA")
    
    if  ministro[2] != 'Discurso de posse':
        lista_ministro_bio.append(ministro[-1])
    elif  ministro[2] == 'Discurso de posse':
        lista_ministro_bio.append(ministro[-2])
  
# pprint(lista_ministro_bio)  
ministro_bio_paragrafo = []
for ministro_bio in lista_ministro_bio:
    # print(type(ministro_bio))
    url = ministro_bio
    html = urlopen(url)
    bsBio = BeautifulSoup(html.read(), 'html.parser')
    # pprint(bsBio)
    bio = bsBio.find('div',attrs={"class":"item-page"})
    for p in bio.find_all('p'):
        if len(p.get_text(strip=True)) == 0:
            p = p.extract()
        else:
            p = p.get_text(strip=True)
            if 'Nascido' in p:
                p.split('Nascido')[1] 
            elif 'Nasceu' in p: 
                p.split ('Nasceu')[1]
            ministro_bio_paragrafo.append(p)


ministro_bio_paragrafo = [el.replace('\xad','') for el in ministro_bio_paragrafo]

print(ministro_bio_paragrafo)

ministro_discurso_posse_paragrafos = []
for ministro_discurso_posse in lista_ministro_discurso_posse:
    try:
        url = ministro_discurso_posse
        html = urlopen(url)
        bsPosse = BeautifulSoup(html.read(), 'html.parser')
        d_posse = bsPosse.find('div',attrs={"class":"item-page"})
        
        p_d_posse = []
        for p in d_posse.find_all('p'):
            
            if p.find('strong'):
                pass
            else:
                #https://stackoverflow.com/questions/10993612/
                p_d_posse.append(p.get_text(strip=True))
        p_d_posse = [el.replace('\xa0',' ') for el in p_d_posse]
        p_d_posse = [string for string in p_d_posse if string != ""]
        ministro_discurso_posse_paragrafos.append(p_d_posse)
    
    except:
        ministro_discurso_posse_paragrafos.append(ministro_discurso_posse)
        
# print(ministro_discurso_posse_paragrafos)
elemento = "Discurso de posse"
insert_na = "NA"
#https://stackoverflow.com/questions/66671363/find-an-element-in-a-sub-list-and-when-this-element-is-found-append-all-other
nova_lista_ministros = []
for sublista in lista_ministros:
    
    if elemento in sublista:
        sublista[2] = "YES"
        nova_lista_ministros.append(sublista)     
    else:
        sublista[2:2] = ["NA"]
        sublista[4:4] = ["NA"]
        nova_lista_ministros.append(sublista)
        
# print(nova_lista_ministros)

def Extract(lst, i):
    x = i
    return [item[x] for item in lst]

data = Extract(lista_ministros, 0)
ministro = Extract(lista_ministros, 1)
discurso_posse = Extract(nova_lista_ministros, 2)
link_bio = Extract(nova_lista_ministros, 3)
link_discurso = Extract(nova_lista_ministros, 4)

df = pd.DataFrame({
    'data': data,
    'ministro': ministro,
    'discurso_posse': discurso_posse,
    'ministro_discurso_posse_paragrafos':ministro_discurso_posse_paragrafos,
    'ministro_bio_paragrafo': ministro_bio_paragrafo,
    'link_bio': link_bio,
    'link_discurso': link_discurso,
    })
df.to_csv('discursos.csv')
print(df.head())
# print(df.to_string())



    
    

