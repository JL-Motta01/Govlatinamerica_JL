from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    pass


def dados():
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-previdencia"
    mt_page = page_access(url)


def cartilhas(): # in progress
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/acesso-a-informacao/cartilha-de-emendas-parlamentares-2022"
    mt_page = page_access(url)
    title_cartilhas = mt_page.find("h1", class_="documentFirstHeading").text
    post_cartilhas = mt_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cartilhas = mt_page.find("span", class_="documentModified").find("span", class_="value").text
    print(title_cartilhas, post_cartilhas, update_cartilhas)
    content_cartilhas = mt_page.find("div", {"id" : "content-core"}).text
    links_cartilhas = mt_page.find("div", {"id":"content-core"}).find_all("article")
    for article_cartilhas in links_cartilhas:
        list_links_cartilhas.append(article_cartilhas.a["href"])
        """
        fraudes_page = page_access(li_fraudes.a["href"])
        title_fraudes_page = fraudes_page.find("h1", class_="documentFirstHeading").text
        post_fraudes_page = fraudes_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_fraudes_page = fraudes_page.find("span", class_="documentModified").find("span", class_="value").text
        content_fraudes_page = fraudes_page.find("div", {"id" : "parent-fieldname-text"}).text
        """


def acordos(): # check - otimizar
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/assuntos/acordos-internacionais/acordos-internacionais"
    mt_page = page_access(url)
    title_acordos = mt_page.find("h1", class_="documentFirstHeading").text
    post_acordos = mt_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_acordos = mt_page.find("span", class_="documentModified").find("span", class_="value").text
    content_acordos = mt_page.find("div", {"id" : "content-core"}).text
    links_acordos = mt_page.find("div", {"id":"content-core"}).find_all("article")
    for article_acordos in links_acordos:
        acordos_page = page_access(article_acordos.a["href"])
        title_acordos_page = acordos_page.find("h1", class_="documentFirstHeading").text
        try:
            post_acordos_page = acordos_page.find("span", class_="documentPublished").find("span", class_="value").text
        except:
            pass
        try:
            update_acordos_page = acordos_page.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        try:
            content_acordos_page = acordos_page.find("div", {"id" : "parent-fieldname-text"}).text
        except:
            pass
        list_links_acordos_page = []
        links_acordos_page = acordos_page.find("div", {"id" : "content-core"}).find_all("a")
        for a_acordos_page in links_acordos_page:
            list_links_acordos_page.append(a_acordos_page["href"])


def fraudes(): # check - otimizar
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/assuntos/assuntos-previdencia/outros/combate-as-fraudes"
    mt_page = page_access(url)
    title_fraudes = mt_page.find("h1", class_="documentFirstHeading").text
    post_fraudes = mt_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_fraudes = mt_page.find("span", class_="documentModified").find("span", class_="value").text
    content_fraudes = mt_page.find("div", {"id" : "parent-fieldname-text"}).text
    links_fraudes = mt_page.find("div", class_="content clearfix").find_all("li")
    for li_fraudes in links_fraudes:
        fraudes_page = page_access(li_fraudes.a["href"])
        title_fraudes_page = fraudes_page.find("h1", class_="documentFirstHeading").text
        post_fraudes_page = fraudes_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_fraudes_page = fraudes_page.find("span", class_="documentModified").find("span", class_="value").text
        content_fraudes_page = fraudes_page.find("div", {"id" : "parent-fieldname-text"}) # contém imagem


def transparencia(): # check
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br/assuntos/assuntos-previdencia/outros/transparencia-nova-previdencia-1"
    mt_page = page_access(url)
    title_transparencia = mt_page.find("h1", class_="documentFirstHeading").text
    post_transparencia = mt_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_transparencia = mt_page.find("span", class_="documentModified").find("span", class_="value").text
    content_transparencia = mt_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_transparencia = []
    links_transparencia = mt_page.find("div", {"id":"content-core"}).find_all("li")
    for li_transparencia in links_transparencia:
        list_links_transparencia.append(li_transparencia.a["href"])


def main():
    global bs
    url = "https://www.gov.br/trabalho-e-previdencia/pt-br"
    bs = page_access(url) 
    # mt_noticias = noticias()
    # mt_dados = dados()
    mt_cartilhas = cartilhas()
    # mt_acordos = acordos()
    # mt_fraudes = fraudes()
    # mt_transparencia = transparencia()



if __name__ == "__main__":
    main()