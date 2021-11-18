from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mma/pt-br/assuntos/noticias" 
    ma_page = page_access(url)


def acoes():
    url = "https://www.gov.br/mma/pt-br/acesso-a-informacao/acoes-e-programas" 
    ma_page = page_access(url)


def infos():
    url = "" 
    ma_page = page_access(url)


def dados():
    url = "" 
    ma_page = page_access(url)


def relatorios():
    url = "" 
    ma_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/mma/pt-br"
    bs = page_access(url) 
    ma_noticias = noticias()   
    ma_acoes = acoes() 
    ma_infos = infos() 
    ma_dados = dados() 
    ma_relatorios = relatorios() 


if __name__ == "__main__":
    main()
