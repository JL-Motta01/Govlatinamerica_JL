from urllib import request
from urllib.request import urlopen
import urllib.parse
from urllib.parse import urlparse
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import csv

## dir_txt = "C:/Users/Pichau/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/testecsv.txt"
dir_txt = "/home/labri_joaomotta/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/testecsv.txt"
csvFile = open(dir_txt,'wt')
url = 'https://www.gov.br/sitemap.xml'
writer = csv.writer(csvFile)
xml= urlopen(url)
bs = BeautifulSoup(xml.read(), 'lxml-xml')
sitemap = bs.find_all("url")
for link in sitemap:
    print (link.find("loc").get_text())
    csvRow = []
    csvRow.append(link.find("loc").get_text())
    filename = xml.url.split("/arquivos")[-1] + '.html'
    with open(filename, 'wb') as f:
        f.write(xml.body)
            
