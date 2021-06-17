import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

csvFile = open("C:/Users/Pichau/codigo/govbr/brasil/govfederal/govbr/arquivos/teste.txt",'wt')
paginas = set()
def getLinks(pageUrl):
    global paginas
    html = urlopen("https://www.gov.br/")
    bsObj = BeautifulSoup(html, features="html.parser")
    writer = csv.writer(csvFile)
    for link in bsObj.findAll("a"):
         if 'href' in link.attrs:
            if link.attrs['href'] not in paginas:
             #nova página encontrada
                newPage = link.attrs['href']
                print(newPage)
                paginas.add(newPage)
                getLinks(newPage)
                csvRow = []
                csvRow.append(newPage)
                writer.writerow(csvRow)
getLinks("")
csvFile.close()  
