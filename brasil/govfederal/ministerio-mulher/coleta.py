from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def infos():
    url = "https://www.gov.br/mdh/pt-br/acesso-a-informacao/informacoes-classificadas"


def dados():
    url = "https://www.gov.br/mdh/pt-br/acesso-a-informacao/dados-abertos/plano-de-dados-abertos-2020-2022"


def publicacoes():
    url = "https://www.gov.br/mdh/pt-br/centrais-de-conteudo/publicacoes"


def noticias():
    pass


def main():
    global bs
    url = "https://www.gov.br/mdh/pt-br"
    bs = page_access(url) 
    mdh_infos = infos()
    mdh_dados = dados()
    mdh_publicacoes = publicacoes()
    mdh_noticias = noticias()


if __name__ == "__main__":
    main()