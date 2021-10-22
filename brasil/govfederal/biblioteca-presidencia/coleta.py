from urllib.request import build_opener, urlopen  # biblioteca nativa
from bs4 import BeautifulSoup  # biblioteca de terceiros


def acessar_pagina(url):
    html = urlopen(url)
    # chama a página
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    # percorre os elementos que queremos
    return bsoup


def links_presidentes(bs):
    presidentes = bs.find("div", id="content").find_all("div", class_="banner-tile tile-content")
    lista_presidentes = []
    for presidente in presidentes:
        lista_presidentes.append(presidente.a["href"])
    print(lista_presidentes)
    return lista_presidentes


def main():
    global bs
    url = "http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/capa-inicial"
    bs = acessar_pagina(url)
    presidentes = links_presidentes(bs)


if __name__ == "__main__":
    main()
