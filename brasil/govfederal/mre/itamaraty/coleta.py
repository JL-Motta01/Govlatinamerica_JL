from urllib.request import build_opener, urlopen  # biblioteca nativa
from bs4 import BeautifulSoup  # biblioteca de terceiros


def nota_imprensa():
    mre_acesso_pagina = acesso_pagina()
    lista_paginas = []


def acesso_pagina():
    html = urlopen("http://www.biblioteca.presidencia.gov.br/")
    bs = BeautifulSoup(html, "html.parser")
    return bs


def main():
    bs = pagina()
    print(bs)


if __name__ == "__main__":
    main()
