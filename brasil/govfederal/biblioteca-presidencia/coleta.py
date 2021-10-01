from urllib.request import build_opener, urlopen  # biblioteca nativa
from bs4 import BeautifulSoup  # biblioteca de terceiros


def pagina():
    html = urlopen("http://www.biblioteca.presidencia.gov.br/")
<<<<<<< HEAD
    # chama a página
=======
    ## chama a página
>>>>>>> 5b57eebc05741e58c5b5abacb830be28770638e3
    bs = BeautifulSoup(html, "html.parser")
    # percorre os elementos que queremos
    return bs


def links_noticias(bs):
    pass


def main():
    bs = pagina()
    ## links = links_noticias(bs)
    print(bs)


if __name__ == "__main__":
    main()
