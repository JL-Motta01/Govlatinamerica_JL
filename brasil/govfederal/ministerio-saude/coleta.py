from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias(): # check
    pass
    # código a ser desenvolvido


def boletins(): # check - ajustar posteriormente
    url_base = "https://www.gov.br/saude/pt-br/assuntos/boletins-epidemiologicos/"
    subpages = ["numeros-anteriores", "numeros-recentes", "por-assunto"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)
        title_boletins = sd_page.find("h1", class_="documentFirstHeading").text
        post_boletins = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_boletins = sd_page.find("span", class_="documentModified").find("span", class_="value").text
        list_links_boletins = []
        links_boletins = sd_page.find("div", {"id" : "content-core"}).find_all("a")
        for a_boletins in links_boletins:
            list_links_boletins.append(a_boletins["href"])


def rename(): # check
    url = "https://www.gov.br/saude/pt-br/assuntos/assistencia-farmaceutica-no-sus/rename"
    sd_page = page_access(url)
    title_rename = sd_page.find("h1", class_="documentFirstHeading").text
    post_rename = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_rename = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_rename = []
    links_rename = sd_page.find("div", {"id":"content-core"}).find_all("a")
    for a_rename in links_rename:
        list_links_rename.append(a_rename["href"])


def arquivos(): # check
    url = "https://www.gov.br/saude/pt-br/assuntos/arquivos"
    sd_page = page_access(url)
    title_arquivos = sd_page.find("h1", class_="documentFirstHeading").text
    post_arquivos = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_arquivos = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    link_arquivos = sd_page.find("div", {"id":"content-core"}).find_all("article")
    for article_arquivos in link_arquivos:
        arquivos_pages = page_access(article_arquivos.h2.a["href"])
        link_arquivos_pages = arquivos_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_arquivos = []
        for a_arquivos_pages in link_arquivos_pages:
            list_link_arquivos.append(a_arquivos_pages["href"])


def vacinas_plano(): # check
    url_base = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/plano-nacional-de-operacionalizacao-da-vacina-contra-a-covid-19/"
    subpages = ["notas-tecnicas", "informes-tecnicos", "notas-informativas", "oficios-circulares"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)
        title_vacinas_plano = sd_page.find("h1", class_="documentFirstHeading").text
        post_vacinas_plano = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_vacinas_plano = sd_page.find("span", class_="documentModified").find("span", class_="value").text
        link_vacinas_plano = sd_page.find("div", {"id":"content-core"}).find_all("article")
        for article_vacinas_plano in link_vacinas_plano:
            vacinas_plano_pages = page_access(article_vacinas_plano.h2.a["href"])
            link_vacinas_plano_pages = vacinas_plano_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_vacinas_plano = []
            for a_vacinas_plano_pages in link_vacinas_plano_pages:
                list_link_vacinas_plano.append(a_vacinas_plano_pages["href"])


def vac_gt(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/grupos-de-trabalho-gt"
    sd_page = page_access(url)
    title_vac_gt = sd_page.find("h1", class_="documentFirstHeading").text
    post_vac_gt = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_vac_gt = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    content_vac_gt = sd_page.find("div", {"id" : "parent-fieldname-text"}).text
    # links
    list_links_vac_gt = []
    links_vac_gt = sd_page.find("div", {"id":"content-core"}).find_all("a")
    for a_vac_gt in links_vac_gt:
        list_links_vac_gt.append(a_vac_gt["href"])


def vac_pdf(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/pdfs"
    sd_page = page_access(url)
    title_vac_pdf = sd_page.find("h1", class_="documentFirstHeading").text
    post_vac_pdf = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_vac_pdf = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    link_vac_pdf = sd_page.find("div", {"id":"content-core"}).find_all("article")
    for article_vac_pdf in link_vac_pdf:
        vac_pdf_pages = page_access(article_vac_pdf.h2.a["href"])
        link_vac_pdf_pages = vac_pdf_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_vac_pdf = []
        for a_vac_pdf_pages in link_vac_pdf_pages:
            list_link_vac_pdf.append(a_vac_pdf_pages["href"])


def vac_sctie(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/relatorios-de-monitoramento-sctie"
    sd_page = page_access(url)
    title_vac_sctie = sd_page.find("h1", class_="documentFirstHeading").text
    post_vac_sctie = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_vac_sctie = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    content_vac_sctie = sd_page.find("div", {"id" : "parent-fieldname-text"}).text
    # links
    list_links_vac_sctie = []
    links_vac_sctie = sd_page.find("div", {"id":"content-core"}).find_all("a")
    for a_vac_sctie in links_vac_sctie:
        list_links_vac_sctie.append(a_vac_sctie["href"])


def acoes(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/acoes-estrategicas"
    sd_page = page_access(url)
    title_acoes = sd_page.find("h1", class_="documentFirstHeading").text
    post_acoes = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_acoes = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_acoes = []
    while counter < 61:
        domain = "https://www.gov.br/saude/pt-br/coronavirus/acoes-estrategicas?b_size=60&b_start:int="
        domain += str(counter) 
        counter += 60
        list_url_acoes.append(domain)
    for url_acoes in list_url_acoes:
        page = page_access(url_acoes)
        content_acoes = page.find("div", {"id":"content-core"}).find_all("li")
        for li_acoes in content_acoes:
            link_acoes = page_access(li_acoes.div.h2.a["href"]) 
            # entrando
            title_link_acoes = link_acoes.find("h1", class_="documentFirstHeading").text
            try:
                post_link_acoes = link_acoes.find("span", class_="documentPublished").find("span", class_="value").text
            except:
                pass
            try:
                update_link_acoes = link_acoes.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_link_acoes = link_acoes.find("div", {"id":"parent-fieldname-text"}).text
            # tags 
            lista_tags_acoes = []
            try: 
                tags_acoes = link_acoes.find("div", {"id":"category"}).find_all("span")
                for span_acoes in tags_acoes:
                    lista_tags_acoes.append(span_acoes.text)
            except:
                lista_tags_acoes.append("boletim sem tag")
            if lista_tags_acoes[0] != 'boletim sem tag' :
                del lista_tags_acoes[0]


def corona_boletins(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/boletins-epidemiologicos"
    sd_page = page_access(url)
    title_corona_boletins = sd_page.find("h1", class_="documentFirstHeading").text
    post_corona_boletins = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_corona_boletins = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_corona_boletins = []
    while counter < 41:
        domain = "https://www.gov.br/saude/pt-br/coronavirus/boletins-epidemiologicos?b_start:int="
        domain += str(counter) 
        counter += 20
        list_url_corona_boletins.append(domain)
    for url_corona_boletins in list_url_corona_boletins:
        page = page_access(url_corona_boletins)
        link_corona_boletins = page.find("div", {"id":"content-core"}).find_all("article")
        for article_corona_boletins in link_corona_boletins:
            corona_boletins_pages = page_access(article_corona_boletins.h2.a["href"])
            link_corona_boletins_pages = corona_boletins_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_corona_boletins = []
            for a_corona_boletins_pages in link_corona_boletins_pages:
                list_link_corona_boletins.append(a_corona_boletins_pages["href"])


def risco_covid(): # check
    url = "https://www.gov.br/saude/pt-br/coronavirus/avaliacao-de-risco-para-covid-19/avaliacao-de-risco-no-cenario-da-covid-19"
    sd_page = page_access(url)
    title_risco_covid = sd_page.find("h1", class_="documentFirstHeading").text
    post_risco_covid = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_risco_covid = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    content_risco_covid = sd_page.find("div", {"id" : "parent-fieldname-text"}).text
    # links
    list_links_risco_covid = []
    links_risco_covid = sd_page.find("div", {"id":"content-core"}).find_all("a")
    for a_risco_covid in links_risco_covid:
        list_links_risco_covid.append(a_risco_covid["href"])


def infos(): # check
    url_base = "https://www.gov.br/saude/pt-br/acesso-a-informacao/informacoes-classificadas/"
    subpages = ["rol-de-informacoes-classificadas", "rol-de-informacoes-desclassificadas"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)
        title_infos = sd_page.find("h1", class_="documentFirstHeading").text
        post_infos = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_infos = sd_page.find("span", class_="documentModified").find("span", class_="value").text
        link_infos = sd_page.find("div", {"id":"content-core"}).find_all("article")
        for article_infos in link_infos:
            infos_pages = page_access(article_infos.h2.a["href"])
            link_infos_pages = infos_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_infos = []
            for a_infos_pages in link_infos_pages:
                list_link_infos.append(a_infos_pages["href"])


def cartilhas(): # check
    url = "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/cartilhas/2018"
    sd_page = page_access(url)
    title_cartilhas = sd_page.find("h1", class_="documentFirstHeading").text
    post_cartilhas = sd_page.find("span", class_="documentPublished").find("span", class_="value").text
    try:
        update_cartilhas = sd_page.find("span", class_="documentModified").find("span", class_="value").text
    except:
        pass
    link_cartilhas = sd_page.find("div", {"id":"content-core"}).find_all("article")
    for article_cartilhas in link_cartilhas:
        cartilhas_pages = page_access(article_cartilhas.h2.a["href"])
        link_cartilhas_pages = cartilhas_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_cartilhas = []
        for a_cartilhas_pages in link_cartilhas_pages:
            list_link_cartilhas.append(a_cartilhas_pages["href"])


def campanhas(): # in progress
    url_base = "https://www.gov.br/saude/pt-br/campanhas-da-saude/"
    subpages = ["2021", "2020", "2019"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)
        print(url)
        # title_campanhas = sd_page.find("h1", class_="documentFirstHeading").text
        # print(title_campanhas)


def main():
    global bs
    url = "https://www.gov.br/saude/pt-br"
    bs = page_access(url) 
    # sd_noticias = noticias()
    # sd_boletins = boletins()
    # sd_rename = rename()
    # sd_arquivos = arquivos()
    # sd_vacinas_plano = vacinas_plano()
    # sd_vac_gt = vac_gt()
    # sd_vac_pdf = vac_pdf()
    # sd_vac_sctie = vac_sctie()
    # sd_acoes = acoes()
    # sd_corona_boletins = corona_boletins()
    # sd_risco_covid = risco_covid()
    # sd_infos = infos()
    # sd_cartilhas = cartilhas()
    sd_campanhas = campanhas()


if __name__ == "__main__":
    main()