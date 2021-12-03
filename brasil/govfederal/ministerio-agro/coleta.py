from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def dados_abertos(): # check
    url_base = "https://www.gov.br/agricultura/pt-br/acesso-a-informacao/dadosabertos" 
    mapa_page = page_access(url_base)
    content_dados_page = mapa_page.find("div", class_="cover-richtext-tile tile-content").text
    subpages = ["/pda-2020-2022", "/pdas-anteriores/pda-2018-2019", "/pdas-anteriores/pda-2016-2017", "/legislacao-dados-abertos"]
    for pages in subpages:
        url = url_base + pages
        mapa_pages = page_access(url)
        title_dados_abertos = mapa_pages.find("h1", class_="documentFirstHeading").text
        post_dados_abertos = mapa_pages.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_dados_abertos = mapa_pages.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_dados_abertos = mapa_pages.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_dados_abertos = []
        links_dados_abertos = mapa_pages.find("div", {"id":"content-core"}).find_all("a")
        for a_dados_abertos in links_dados_abertos:
            list_links_dados_abertos.append(a_dados_abertos["href"])


def demons_contab(): # check
    url = "https://www.gov.br/agricultura/pt-br/acesso-a-informacao/demonstrativos-contabeis"
    mapa_page = page_access(url)
    title_demons_contab = mapa_page.find("h1", class_="documentFirstHeading").text
    post_demons_contab = mapa_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_demons_contab = mapa_page.find("span", class_="documentModified").find("span", class_="value").text
    content_demons_contab = mapa_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_demons_contab = []
    links_demons_contab = mapa_page.find("div", {"id":"content-core"}).find_all("a")
    for a_demons_contab in links_demons_contab:
        list_links_demons_contab.append(a_demons_contab["href"])


def main():
    global bs
    url = "https://www.gov.br/agricultura/pt-br"
    bs = page_access(url) 
    mapa_dados_abertos = dados_abertos()
    mapa_demons_contab = demons_contab()



if __name__ == "__main__":
    main()