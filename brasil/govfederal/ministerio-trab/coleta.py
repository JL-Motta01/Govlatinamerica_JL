from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    pass


def main():
    global bs
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br"
    bs = page_access(url) 
    # mt_noticias = noticias()

if __name__ == "__main__":
    main()