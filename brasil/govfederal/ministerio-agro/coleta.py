from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
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


def infos(): # check
    url = "https://www.gov.br/agricultura/pt-br/acesso-a-informacao/informacoes-classificadas"
    mapa_page = page_access(url)
    title_infos = mapa_page.find("h1", class_="documentFirstHeading").text
    post_infos = mapa_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos = mapa_page.find("span", class_="documentModified").find("span", class_="value").text
    content_infos = mapa_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_infos = []
    links_infos = mapa_page.find("div", {"id":"content-core"}).find_all("a")
    for a_infos in links_infos:
        list_links_infos.append(a_infos["href"])  


def transparencia(): # check
    url_base = "https://www.gov.br/agricultura/pt-br/acesso-a-informacao/transparencia/"
    anos = ["auditoria-2007", "exercicio-2008", "exercicio-2009", "exercicio-2010", "exercicio-2011", "exercicio-2012", "exercicio-2013", "exercicio-2014", "exercicio-2015", "exercicio-2016", "exercicio-2017", "exercicio-2018", "exercicio-2019", "exercicio-2020", "exercicio-2021"]
    for ano in anos:
        url = url_base + ano
        mapa_page = page_access(url)  
        title_transparencia = mapa_page.find("h1", class_="documentFirstHeading").text
        post_transparencia = mapa_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_transparencia = mapa_page.find("span", class_="documentModified").find("span", class_="value").text
        content_transparencia = mapa_page.find("div", {"id":"parent-fieldname-text"}).text
        # links
        list_links_transparencia = []
        links_transparencia = mapa_page.find("div", {"id":"content-core"}).find_all("a")
        for a_transparencia in links_transparencia:
            list_links_transparencia.append(a_transparencia["href"])  


def noticias(): # check
    pass
    # código a ser desenvolvido


def crise(): # check
    url = "https://www.gov.br/agricultura/pt-br/campanhas/mapacontracoronavirus/documentos/comite-de-crise"
    mapa_page = page_access(url)  
    title_crise = mapa_page.find("h1", class_="documentFirstHeading").text
    post_crise = mapa_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_crise = mapa_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_crise = []
    links_crise = mapa_page.find("div", {"id":"content-core"}).find_all("a")
    for a_crise in links_crise:
        list_links_crise.append(a_crise["href"])


def atividades(): # check
    url = "https://www.gov.br/agricultura/pt-br/campanhas/mapacontracoronavirus/documentos/atividades-essenciais"
    mapa_page = page_access(url) 
    title_atividades = mapa_page.find("h1", class_="documentFirstHeading").text
    post_atividades = mapa_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_atividades = mapa_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_atividades = []
    links_atividades = mapa_page.find("div", {"id":"content-core"}).find_all("a")
    for a_atividades in links_atividades:
        list_links_atividades.append(a_atividades["href"])


def main():
    global bs
    url = "https://www.gov.br/agricultura/pt-br"
    bs = page_access(url) 
    mapa_dados_abertos = dados_abertos()
    mapa_demons_contab = demons_contab()
    mapa_infos = infos()
    mapa_transparencia = transparencia()
    mapa_noticias = noticias()
    mapa_crise = crise()
    mapa_atividades = atividades()


if __name__ == "__main__":
    main()