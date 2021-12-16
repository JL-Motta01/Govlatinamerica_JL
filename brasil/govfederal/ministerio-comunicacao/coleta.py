from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mcom/pt-br/noticias"
    pass


def dados():
    url = "https://www.gov.br/mcom/pt-br/acesso-a-informacao/dados-abertos"
    mcom_page = page_access(url)


def publicacoes():
    url = "https://www.gov.br/mcom/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/publicacoes"
    mcom_page = page_access(url)


def cartilha():
    url = "https://www.gov.br/mcom/pt-br/assuntos/cartilha-programas-mcom-emendas-2021"
    mcom_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/mcom/pt-br"
    bs = page_access(url) 
    # mcom_noticias = noticias()
    # mcom_dados = dados()
    # mcom_publicacoes = publicacoes()
    # mcom_cartilha = cartilha()


if __name__ == "__main__":
    main()