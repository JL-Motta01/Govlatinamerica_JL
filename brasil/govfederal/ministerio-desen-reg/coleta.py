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


def dados(): # check
    url = "https://www.gov.br/mdr/pt-br/acesso-a-informacao/dados-abertos"
    mdr_page = page_access(url)
    title_dados = mdr_page.find("h1", class_="documentFirstHeading").text
    post_dados = mdr_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados = mdr_page.find("span", class_="documentModified").find("span", class_="value").text
    list_links_dados = []
    links_dados = mdr_page.find("div", {"id":"content-core"}).find_all("a")
    for a_dados in links_dados:
        list_links_dados.append(a_dados["href"])
    del(list_links_dados[0])
    del(list_links_dados[1::])


def transparencia(): # check
    url = "https://www.gov.br/mdr/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas"
    mdr_page = page_access(url)
    title_transparencia = mdr_page.find("h1", class_="documentFirstHeading").text
    post_transparencia = mdr_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_transparencia = mdr_page.find("span", class_="documentModified").find("span", class_="value").text
    content_transparencia = mdr_page.find("div", {"id":"parent-fieldname-text"}).text
    list_links_transparencia = []
    links_transparencia = mdr_page.find("div", {"id":"content-core"}).find_all("a")
    for a_transparencia in links_transparencia:
        list_links_transparencia.append(a_transparencia["href"])


def publicacoes(): # check - otimizar seleção de links
    url = "https://www.gov.br/mdr/pt-br/centrais-de-conteudo/publicacoes/publicacoes-mdr"
    mdr_page = page_access(url)
    title_publicacoes = mdr_page.find("h1", class_="documentFirstHeading").text
    post_publicacoes = mdr_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_publicacoes = mdr_page.find("span", class_="documentModified").find("span", class_="value").text
    list_links_publicacoes = []
    links_publicacoes = mdr_page.find("div", {"id":"content-core"}).find_all("a")
    for a_publicacoes in links_publicacoes:
        list_links_publicacoes.append(a_publicacoes["href"])


def main():
    global bs
    url = "https://www.gov.br/mdr/pt-br"
    bs = page_access(url) 
    # mdr_noticias = noticias()
    # mdr_dados = dados()
    # mdr_transparencia = transparencia()
    mdr_publicacoes = publicacoes()


if __name__ == "__main__":
    main()