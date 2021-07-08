from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
#from iteration_utilities import split
import re
import unicodedata
import requests

page = requests.get('https://www.funag.gov.br/chdd/index.php/ministros-de-estado-das-relacoes-exteriores')

soup = BeautifulSoup(page.content, 'html.parser')


autor = [a.get_text() for a in  ]
autor_link
discurso
discurso_link
