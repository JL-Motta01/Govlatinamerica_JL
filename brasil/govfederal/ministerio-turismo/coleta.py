from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/turismo/pt-br/assuntos/noticias"
    pass


def corona():
    url = "https://www.gov.br/turismo/pt-br/assuntos/coronavirus"
    mtur_page = page_access(url)


def acordos():
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/acordos"
    mtur_page = page_access(url)


def cartilha():
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/cartilha-parlamentar"
    mtur_page = page_access(url)


def pesquisas():
    url = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/pesquisas"
    mtur_page = page_access(url)


def noticias_secre():
    url = "https://www.gov.br/turismo/pt-br/secretaria-especial-da-cultura/assuntos/noticias"
    mtur_page = page_access(url)


def cartilha_lit():
    url = "https://www.gov.br/turismo/pt-br/secretaria-especial-da-cultura/centrais-de-conteudo/publicacoes/livro-leitura-literatura-e-bibliotecas/cartilhas-2"
    mtur_page = page_access(url)


def main():
    global bs
    url = ""
    bs = page_access(url) 
    # mtur_noticias = noticias()
    # mtur_corona = corona()
    # mtur_acordos = acordos()
    # mtur_cartilha = cartilha()
    # mtur_pesquisas = pesquisas()
    # mtur_noticias_secre = noticias_secre()
    # mtur_cartilha_lit = cartilha_lit()


if __name__ == "__main__":
    main()