from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests 

url = input("https://www.gov.br/mre/pt-br")
page = requests.get("https://www.gov.br/mre/pt-br")
soup = BeautifulSoup(page.content, 'html.parser')
