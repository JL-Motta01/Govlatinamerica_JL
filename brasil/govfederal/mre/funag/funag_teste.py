from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

url = "https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores?layout=edit&id=450"
html = urlopen(url)
bsPosse = BeautifulSoup(html.read(), 'html.parser')

d_posse = bsPosse.find('div',attrs={"class":"item-page"})
# print(d_posse)
p_d_posse = []
for p in d_posse.find_all('p'):
    if p.find('strong'):
        pass
    else:
        #https://stackoverflow.com/questions/10993612/
        p_d_posse.append(p.get_text(strip=True))
        
 #https://stackoverflow.com/questions/3883030       
# p_d_posse = [elem if '\xa0' not in elem else elem.replace('\xa0', '') for elem in p_d_posse]
p_d_posse = [el.replace('\xa0',' ') for el in p_d_posse]
#https://www.kite.com/python/answers/how-to-remove-empty-strings-from-a-list-of-strings-in-python
p_d_posse = [string for string in p_d_posse if string != ""]

print(p_d_posse)



    
# mydiv = soup.find("div", { "class" : "" })
# for p in mydiv.find_all('p'):
#     text_list.append(p.get_text())