from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mdr/pt-br/noticias"
    pass


def infos():
    url = "https://www.gov.br/mdr/pt-br/acesso-a-informacao/informacoes-classificadas"
    mdr_page = page_access(url)


def dados():
    url = "https://www.gov.br/mdr/pt-br/acesso-a-informacao/dados-abertos"
    mdr_page = page_access(url)


def transparencia():
    url = "https://www.gov.br/mdr/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas"
    mdr_page = page_access(url)


def publicacoes():
    url = "https://www.gov.br/mdr/pt-br/centrais-de-conteudo/publicacoes/publicacoes-mdr"
    mdr_page = page_access(url)


def main():
    global bs
    url = ""
    bs = page_access(url) 
    # mdr_noticias = noticias()
    # mdr_infos = infos()
    # mdr_dados = dados()
    # mdr_transparencia = transparencia()
    # mdr_publicacoes = publicacoes()


if __name__ == "__main__":
    main()