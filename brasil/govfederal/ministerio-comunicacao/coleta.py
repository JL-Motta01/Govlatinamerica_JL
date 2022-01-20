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


def dados(): # check
    url = "https://www.gov.br/mcom/pt-br/acesso-a-informacao/dados-abertos/bases-abertas"
    mcom_page = page_access(url)
    title_dados = mcom_page.find("h1", class_="documentFirstHeading").text
    post_dados = mcom_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados = mcom_page.find("span", class_="documentModified").find("span", class_="value").text
    content_dados = mcom_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_dados = []
    links_dados = mcom_page.find("div", {"id":"content-core"}).find_all("a")
    for a_dados in links_dados:
        list_links_dados.append(a_dados["href"])
    del (list_links_dados[0])
    del (list_links_dados[3])


def publicacoes(): # check
    url_base = "https://www.gov.br/mcom/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/publicacoes/"
    pages = ["editais", "multas"]
    for page in pages:
        url = url_base + page
        mcom_page = page_access(url)
        title_publicacoes = mcom_page.find("h1", class_="documentFirstHeading").text
        post_publicacoes = mcom_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_publicacoes = mcom_page.find("span", class_="documentModified").find("span", class_="value").text
        list_link_publicacoes = []
        link_publicacoes = mcom_page.find("div", {"id":"content-core"}).find_all("a")
        for a_publicacoes in link_publicacoes:
            list_link_publicacoes.append(a_publicacoes["href"])


def cartilha(): # check
    url = "https://www.gov.br/mcom/pt-br/assuntos/cartilha-programas-mcom-emendas-2021"
    mcom_page = page_access(url)
    title_cartilha = mcom_page.find("h1", class_="documentFirstHeading").text
    post_cartilha = mcom_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cartilha = mcom_page.find("span", class_="documentModified").find("span", class_="value").text
    list_link_cartilha = []
    link_cartilha = mcom_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cartilha in link_cartilha:
        list_link_cartilha.append(a_cartilha["href"]) 


def main():
    global bs
    url = "https://www.gov.br/mcom/pt-br"
    bs = page_access(url) 
    mcom_noticias = noticias()
    mcom_dados = dados()
    mcom_publicacoes = publicacoes()
    mcom_cartilha = cartilha()


if __name__ == "__main__":
    main()