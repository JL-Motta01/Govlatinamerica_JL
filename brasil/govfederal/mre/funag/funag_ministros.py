from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
#from iteration_utilities import split
import re
import unicodedata
import lxml

url = 'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores'
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
links = []
datas = []
autores = []

for link in bs.find_all('a', string='Discurso de posse'):
    # print(urllib.parse.urljoin(url, link.get('href')))
    links.append(urllib.parse.urljoin(url, link.get('href')))
# print(len(links))

for data in bs.find_all('strong'):
    datas.append(data.get_text())

datas_tmp2 = datas[2:]
# datas_tmp = list(dict.fromkeys(datas_tmp))
data_tmp2 = "".join([str(_) for _ in datas_tmp2])
data_tmp2 = unicodedata.normalize("NFKD", data_tmp2)
data_tmp2 = re.split("(\d{2}[-/]\d{2}[-/]\d{4})", data_tmp2)
data_tmp2 = [x for x in data_tmp2 if x != '']
data_tmp2 = [elem for elem in data_tmp2 if elem.strip()]
datas_final = list(set(data_tmp2))


for autor in bs.find_all('a'):
    autores.append(autor.get_text())

# print(links)


autores_final = []
for autor in autores:
    """
    tratamento para extrair lista dos ministros
    """
    inicio = 'Carlos Alberto Franco França'
    final = 'Ministros das Relações Exteriores'
    index_inicio = autores.index(inicio)
    index_final = autores.index(final)
    a = autores[index_inicio:index_final]
    a = [x for x in a if x != 'Discurso de posse']
    autores_final = a

#content-section > div > div.item-page > p:nth-child(48) > a
#content-section > div > div.item-page > p:nth-child(63) > a(1)
# links_bio = []
# p = bs.find_all('p')
# for link_bio in p:
#     a = link_bio.find('a') 
#     links_bio.append(a)

parags = bs.find_all('p')

texto = []

for parag in parags:
    parag = str(parag)
    bsi = BeautifulSoup(parag, "lxml")
    
    tmp=[]
    #extrai textos dos paragrafos
    for string in bsi.stripped_strings:
        palavras = repr(string)
        tmp.append(palavras)
    
    texto.append(tmp) 
    #extri links dos paragrafos
    for link in bsi.find_all("a"):
        links = link['href']
        tmp.append(links)
    texto.append(tmp)


texto2 = texto
#https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
#retira strings de lista de lista
#https://stackoverflow.com/questions/19220554/python-remove-elements-from-nested-lists
texto2 = [[i for i in texto if i != "'|'"] for texto in texto2]
print(texto2[8:-6])
#retira caracter de lista de lista
# https://stackoverflow.com/questions/31794610/removing-a-character-from-a-string-in-a-list-of-lists
texto2 = [[item.replace("'", "") for item in texto] for texto in texto2]

print(texto2[8:-6])

        
        

    

#print(datas_final, "########", autores_final, "#####", links, "#############",links_bio)


# df = pd.DataFrame({
#     'data': datas_final,
#     'autores': autores_final

#     })

# df.to_csv('discursos.csv')
# print(df)

# for i in bs.find_all('p'):
#     print(i.get_text(separator=',', strip=True))
#     print(i.name)
    

# all_results = str(bs.select('p:nth-child()'[0]))
# bs = BeautifulSoup(all_results, 'lxml')
# print(bs.text)
# # print(all_results)
# links = [a['href'] for a in bs.select('a[href]')]
# print(links)

# for li in bs.select('p'):
#     foo = li.select('a'[1])
#     bar = li.select('a'[2])
    
# print(foo,bar,baz)
#content-section > div > div.item-page > p:nth-child(8) > a:nth-child(2)
#content-section > div > div.item-page > p:nth-child(7) > a:nth-child(2)
#content-section > div > div.item-page > p:nth-child(7) > a:nth-child(3)
# items = [item.text for item in bs.select('p:nth-child(odd)')]
# print(items)
#content-section > div > div.item-page > p:nth-child(7) > strong
#content-section > div > div.item-page > p:nth-child(7)
#content-section > div > div.item-page > p:nth-child(8)
#content-section > div > div.item-page > p:nth-child(9)


# paragrafos = []

# for discurso in links:
#     html = urllib.request.urlopen(discurso)
#     bs = BeautifulSoup(html, 'html.parser')
#     for p in bs.find_all('p'):
#         # print(p.get_text())
#         paragrafos.append(p.get_text())


# a = paragrafos
# b = 'Desenvolvido com o CMS de código aberto Joomla'
# # print(paragrafos)
# c = list(filter(None, split(a, b, eq=True)))

# #print(c)
# discursos = []
# datas = []
# for discurso in c:
#     try:
#         finalizar1 = [i for i in discurso if re.search(r'\d*\ DE \b.*?\b DE \d*', i) ]
#         finalizar = ''.join(finalizar1)
#         print(discurso)
#         print(finalizar)
#         index = discurso.index(finalizar)

#         if finalizar:
#             data = discurso.pop(index)
#             datas.append(data)
#             info_list= discurso[0:index]
#             del discurso[0:index]
#             discurso = '#####'.join(discurso)
#             discursos.append(discurso)
#         else:
#             data = 'NA'
#             datas.append(data)
#             info_list= 'NA'
#             #del discurso[0:index]
#             discurso = '#####'.join(discurso)
#             discursos.append(discurso)
#     except ValueError as error:
#         print(error)
# #print (data, info_list, discurso)

# df = pd.DataFrame({
#     'texto': discursos,
#     'data': datas,
#     })
# print(df.head())
# print(df.to_string())
# df.to_csv('discursos.csv')
