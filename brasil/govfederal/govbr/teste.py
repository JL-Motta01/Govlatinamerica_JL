
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


paginas = set()
def getLinks(pageUrl):
    global paginas
    html = urlopen("https://www.gov.br/")
    bsObj = BeautifulSoup(html, features="html.parser")
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            if link.attrs['href'] not in paginas:
             #nova página encontrada
                newPage = link.attrs['href']
                print(newPage)
                paginas.add(newPage)
                getLinks(newPage)
getLinks("")
