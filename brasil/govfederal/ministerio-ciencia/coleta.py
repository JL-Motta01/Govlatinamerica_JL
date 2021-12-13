from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    pass


def boletins(): # check
    url = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/boletins-diarios-mcti/boletins-diarios-mcti"
    mcti_page = page_access(url)
    title_boletins = mcti_page.find("h1", class_="documentFirstHeading").text
    post_boletins = mcti_page.find("span", class_="documentPublished").find("span", class_="value").text
    try:
        update_boletins = mcti_page.find("span", class_="documentModified").find("span", class_="value").text
    except:
        pass
    counter = 0 
    list_url_boletins = []
    while counter < 331:
        domain = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/boletins-diarios-mcti/boletins-diarios-mcti?b_start:int="
        domain += str(counter) 
        counter += 30
        list_url_boletins.append(domain)
    for url_boletins in list_url_boletins:
        page = page_access(url_boletins)
        link_boletins = page.find("div", {"id":"content-core"}).find_all("article")
        for article_boletins in link_boletins:
            boletins_pages = page_access(article_boletins.h2.a["href"])
            link_boletins_pages = boletins_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_boletins = []
            for a_boletins_pages in link_boletins_pages:
                list_link_boletins.append(a_boletins_pages["href"])


def entregas(): # in progress - do it later
    url_base = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/entregas"
    anos = ["/2021", "/2020", "/2019"]
    for ano in anos:
        url = url_base + ano
        mcti_page = page_access(url)


def informes_corona(): # check
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-coronaomicabr-mcti"
    mcti_page = page_access(url)
    title_informes_corona = mcti_page.find("h2", class_="outstanding-title").text
    link_informes_corona = mcti_page.find("div", {"id":"content"}).find_all("div", class_="nitf-basic-tile tile-content")
    for div_informes_corona in link_informes_corona:
        informes_corona_pages = page_access(div_informes_corona.h2.a["href"])
        title_informe_corona = informes_corona_pages.find("h1", class_="documentFirstHeading").text
        post_informe_corona = informes_corona_pages.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_informe_corona = informes_corona_pages.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_informe_corona = informes_corona_pages.find("div", {"id" : "parent-fieldname-text"}).text
        list_links_informes_corona = []
        links_informes_corona = informes_corona_pages.find("div", {"id":"content-core"}).find_all("a")
        for a_informes_corona in links_informes_corona:
            list_links_informes_corona.append(a_informes_corona["href"])


def informes_previr(): # check
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-previr-mcti"
    mcti_page = page_access(url)
    title_informes_previr = mcti_page.find("h2", class_="outstanding-title").text
    link_informes_previr = mcti_page.find("div", {"id":"content"}).find_all("div", class_="nitf-basic-tile tile-content")
    for div_informes_previr in link_informes_previr:
        informes_previr_pages = page_access(div_informes_previr.h2.a["href"])
        title_informe_previr = informes_previr_pages.find("h1", class_="documentFirstHeading").text
        post_informe_previr = informes_previr_pages.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_informe_previr = informes_previr_pages.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_informe_previr = informes_previr_pages.find("div", {"id" : "parent-fieldname-text"}).text
        list_links_informes_previr = []
        links_informes_previr = informes_previr_pages.find("div", {"id":"content-core"}).find_all("a")
        for a_informes_previr in links_informes_previr:
            list_links_informes_previr.append(a_informes_previr["href"])


def informes_humanidade(): # CONFERIR !!
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-covid-19-humanidades-mcti"
    mcti_page = page_access(url)
    title_informes_humanidade = mcti_page.find("h2", class_="outstanding-title").text
    link_informes_humanidade = mcti_page.find("div", {"id":"content"}).find_all("div", class_="nitf-basic-tile tile-content")
    for div_informes_humanidade in link_informes_humanidade:
        informes_humanidade_pages = page_access(div_informes_humanidade.h2.a["href"])
        title_informe_humanidade = informes_humanidade_pages.find("h1", class_="documentFirstHeading").text
        print(title_informe_humanidade)
        post_informe_humanidade = informes_humanidade_pages.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_informe_humanidade = informes_humanidade_pages.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_informe_humanidade = informes_humanidade_pages.find("div", {"id" : "parent-fieldname-text"}).text
        list_links_informes_humanidade = []
        links_informes_humanidade = informes_humanidade_pages.find("div", {"id":"content-core"}).find_all("a")
        for a_informes_humanidade in links_informes_humanidade:
            list_links_informes_humanidade.append(a_informes_humanidade["href"])
        print(list_links_informes_humanidade)


def informes_humanidade():
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-covid-19-humanidades-mcti"
    mcti_page = page_access(url)


def informes_economia():
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-clima-subrede-economia"
    mcti_page = page_access(url)


def informes_variante():
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-redevirus-mcti-variante-omicron"
    mcti_page = page_access(url)


def infos():
    url = "https://www.gov.br/mcti/pt-br/acesso-a-informacao/informacoes-classificadas"
    mcti_page = page_access(url)


def dados():
    url = "https://www.gov.br/mcti/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-1"
    mcti_page = page_access(url)


def comunicados():
    url = "https://www.gov.br/mcti/pt-br/centrais-de-conteudo/comunicados-mcti"
    mcti_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/mcti/pt-br"
    bs = page_access(url) 
    # mcti_noticias = noticias()
    # mcti_boletins = boletins()
    # mcti_entregas = entregas()
    # mcti_informes_corona = informes_corona()
    # mcti_informes_previr = informes_previr()
    mcti_informes_humanidade = informes_humanidade()
    # mcti_informes_economia = informes_economia()
    # mcti_informes_variante = informes_variante()
    # mcti_infos = infos()
    # mcti_dados = dados()
    # mcti_comunicados = comunicados()


if __name__ == "__main__":
    main()