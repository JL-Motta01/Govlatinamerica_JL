import csv
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import requests

csvFile = open("/home/lantri_rafael/codigo/govlatinamerica/brasil/govfederal/govbr/teste.txt",'wt')
paginas = set()
def getLinks(pageUrl):
    global paginas
    url = requests.get("https://www.gov.br/"+pageUrl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})
    html = url.text
    bsObj = BeautifulSoup(html, "html.parser")
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
