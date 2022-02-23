import requests
from bs4 import BeautifulSoup

def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, "html.parser")
    # print(bs)
    return bs

def extrair_info():
    bs = acessar_pagina("https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/")
    tag_h1 = bs.find("h1").text
    print(tag_h1)


def main():
    extrair_info()


if __name__ == "__main__":
    main()