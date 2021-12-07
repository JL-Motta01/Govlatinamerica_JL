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


def boletins():
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
        remove_link = "https://antigo.saude.gov.br"
        while remove_link in list_links_boletins:
            list_links_boletins.remove(remove_link)


def rename():
    url = "https://www.gov.br/saude/pt-br/assuntos/assistencia-farmaceutica-no-sus/rename"
    sd_page = page_access(url)


def arquivos():
    url = "https://www.gov.br/saude/pt-br/assuntos/arquivos"
    sd_page = page_access(url)


def vacinas_plano():
    url_base = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/plano-nacional-de-operacionalizacao-da-vacina-contra-a-covid-19/"
    subpages = ["notas-tecnicas", "informes-tecnicos", "notas-informativas", "oficios-circulares"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)


def vac_gt():
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/grupos-de-trabalho-gt"
    sd_page = page_access(url)


def vac_pdf():
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/pdfs"
    sd_page = page_access(url)


def vac_sctie():
    url = "https://www.gov.br/saude/pt-br/coronavirus/vacinas/relatorios-de-monitoramento-sctie"
    sd_page = page_access(url)


def acoes():
    url = "https://www.gov.br/saude/pt-br/coronavirus/acoes-estrategicas"
    sd_page = page_access(url)


def corona_boletins():
    url = "https://www.gov.br/saude/pt-br/coronavirus/boletins-epidemiologicos"
    sd_page = page_access(url)


def risco_covid():
    url = "https://www.gov.br/saude/pt-br/coronavirus/avaliacao-de-risco-para-covid-19/avaliacao-de-risco-no-cenario-da-covid-19"
    sd_page = page_access(url)


def infos():
    url_base = "https://www.gov.br/saude/pt-br/acesso-a-informacao/informacoes-classificadas/"
    subpages = ["rol-de-informacoes-classificadas", "rol-de-informacoes-desclassificadas"]
    for pages in subpages:
        url = url_base + pages
        sd_page = page_access(url)


def cartilhas():
    url = "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/cartilhas/2018"
    sd_page = page_access(url)


def campanhas():
    url = "https://www.gov.br/saude/pt-br/campanhas-da-saude"
    sd_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/saude/pt-br"
    bs = page_access(url) 
    sd_noticias = noticias()
    sd_boletins = boletins()
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
    # sd_campanhas = campanhas()


if __name__ == "__main__":
    main()