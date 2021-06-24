from urllib.request import urlopen
import urllib.parse
import lxml
from bs4 import BeautifulSoup
import pandas as pd


url = 'C:/Users/Pichau/codigo/govlatinamerica/brasil/govfederal/govbr/arquivos/sitemap.xml'
with open(url,"r") as page:
    bs=BeautifulSoup(page,"lxml")
    sitemap = bs.find_all("url")
    for link in sitemap:
        print (link.find("loc").get_text())
