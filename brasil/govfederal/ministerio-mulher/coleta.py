from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def infos(): # check
    url = "https://www.gov.br/mdh/pt-br/acesso-a-informacao/informacoes-classificadas"
    mdh_page = page_access(url)
    title_infos = mdh_page.find("h1", class_="documentFirstHeading").text
    post_infos = mdh_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos = mdh_page.find("span", class_="documentModified").find("span", class_="value").text
    content_infos = mdh_page.find("div", {"id" : "parent-fieldname-text"}).text
    # links
    list_links_infos = []
    links_infos = mdh_page.find("div", {"id":"content-core"}).find_all("a")
    for a_infos in links_infos:
        list_links_infos.append(a_infos["href"])


def dados(): # check
    url = "https://www.gov.br/mdh/pt-br/acesso-a-informacao/dados-abertos/plano-de-dados-abertos-2020-2022"
    mdh_page = page_access(url)
    title_dados = mdh_page.find("h1", class_="documentFirstHeading").text
    post_dados = mdh_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados = mdh_page.find("span", class_="documentModified").find("span", class_="value").text
    content_dados = mdh_page.find("div", {"id" : "parent-fieldname-text"}).text
    # links
    list_links_dados = []
    links_dados = mdh_page.find("div", {"id":"content-core"}).find_all("p", class_="callout")
    for p_dados in links_dados:
        list_links_dados.append(p_dados.a["href"])


def publicacoes(): # check
    url = "https://www.gov.br/mdh/pt-br/centrais-de-conteudo/publicacoes"
    mdh_page = page_access(url)
    title_publicacoes = mdh_page.find("h1", class_="documentFirstHeading").text
    try: 
        post_publicacoes = mdh_page.find("span", class_="documentPublished").find("span", class_="value").text
    except:
        pass
    update_publicacoes = mdh_page.find("span", class_="documentModified").find("span", class_="value").text
    content_publicacoes = mdh_page.find("div", {"id" : "content-core"}).text
    link_publicacoes = mdh_page.find("div", {"id":"content-core"}).find_all("article")
    for article_publicacoes in link_publicacoes:
        publicacoes_pages = page_access(article_publicacoes.h2.a["href"])
        link_publicacoes_pages = publicacoes_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_publicacoes = []
        for a_publicacoes_pages in link_publicacoes_pages:
            list_link_publicacoes.append(a_publicacoes_pages["href"])


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