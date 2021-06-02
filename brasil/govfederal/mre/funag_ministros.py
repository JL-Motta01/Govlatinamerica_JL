from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from iteration_utilities import split
import re


url = 'https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores'
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser', from_encoding="iso-8859-1")
links = []
datas = []
autores = []

for link in bs.find_all('a', string='Discurso de posse'):
    # print(urllib.parse.urljoin(url, link.get('href')))
    links.append(urllib.parse.urljoin(url, link.get('href')))

for data in bs.find_all('strong'):
    datas.append(data.get_text())

for autor in bs.find_all('a'):
    autores.append(autor.get_text())

# print(links)
# print(autores)

for autor in autores:
    """tratamento para extrair lista dos ministros"""
    inicio = 'Carlos Alberto Franco França'
    final = 'Ministros das RelaÃ§Ãµes Exteriores'
    index_inicio = autores.index(inicio)
    index_final = autores.index(final)
    nova_lista = autores[index_inicio:index_final]


print(list(dict.fromkeys(nova_lista)))


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
