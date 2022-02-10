import requests
from bs4 import BeautifulSoup ## biblioteca de terceiros 

def acessar_pagina(url):
    html = requests.get(url)
    http_code = html.status_code
    bs = BeautifulSoup(html.text, "html.parser")
    return bs, http_code

def recorrer_pagina():
    url_base = 'https://www.bbc.com/portuguese/topics/cz74k717pw5t/page/'
    # https://www.bbc.com/portuguese/topics/cz74k717pw5t/page/100
    lista_urls = []
    contador = 1
    while contador < 20:
        url_final = url_base + str(contador)
        contador += 1
        #print(url_final)
        lista_urls.append(url_final)

def link_noticia():
    for url in lista_urls:
        print(f'URL: {url}')
        pagina = acessar_pagina(url)[0]
        a_noticia = pagina.find("div", class_="lx-stream qa-stream gs-u-box-size gs-t-news").find_all("a", class_="qa-story-cta-link")
        for link in a_noticia:
            link_base = 'https://www.bbc.com'
            noticia_link = link_base + link["href"] 
            print(f'LINK NOTICIA: {noticia_link}')