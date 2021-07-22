from urllib.request import urlopen
import urllib.parse
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import csv

csvFile = open("C:/Users/Pichau/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/testecsv.txt",'wt')
url = 'https://www.gov.br/sitemap.xml'
writer = csv.writer(csvFile)
with open(url,"r") as page:
    bs=BeautifulSoup(page,"lxml")
    sitemap = bs.find_all("url")
    for link in sitemap.find_all("noticias", recursive=True):
        print (link.find("loc").get_text())
        csvRow = []
        csvRow.append(link.find("loc").get_text())
        writer.writerow(csvRow)
        filename = page.url.split("/arquivos")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(page.body)
        yield {'url': page.url}
