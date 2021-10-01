from urllib.request import urlopen
# ativa a biblioteca nativa do python 
from bs4 import BeautifulSoup
# ativa a biblioteca de terceiros que percorre a página, extraindo infos que queremos 

def pagina():
    html = urlopen("http://www.biblioteca.presidencia.gov.br/")
    ## chama a página
    bs = BeautifulSoup(html, "html.parser")
    ## percorre os elementos que queremos
    return bs

def links_noticias(bs):
    pass

def main():
    bs = pagina()
    ## links = links_noticias(bs)
    print(bs)


if __name__ == "__main__" :
    main ()