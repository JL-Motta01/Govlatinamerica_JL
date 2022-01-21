from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mre/pt-br/assuntos/noticias/o-brasil-no-mundo"
    pass


def estudos_mercado_tecnologia(): # check
    url = "https://www.gov.br/mre/pt-br/assuntos/ciencia-tecnologia-e-inovacao/estudos-de-mercado-e-de-tecnologias"
    mre_page = page_access(url)
    title_estudos_mercado_tecnologia = mre_page.find("h1", class_="documentFirstHeading").text
    post_estudos_mercado_tecnologia = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_estudos_mercado_tecnologia = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_estudos_mercado_tecnologia = mre_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_estudos_mercado_tecnologia = []
    links_estudos_mercado_tecnologia = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_estudos_mercado_tecnologia in links_estudos_mercado_tecnologia:
        list_links_estudos_mercado_tecnologia.append(a_estudos_mercado_tecnologia["href"])


def alertas_consular(): # check
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/alertas/alertas"
    mre_page = page_access(url)
    title_alertas_consular = mre_page.find("h1", class_="documentFirstHeading").text
    post_alertas_consular = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_alertas_consular = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_alertas_consular = mre_page.find("div", {"id":"content-core"}).find_all("article")
    for article_alertas_consular in content_alertas_consular:
        link_alertas_consular = page_access(article_alertas_consular.div.h2.a["href"]) 
        title_link_alertas_consular_page = link_alertas_consular.find("h1", class_="documentFirstHeading").text
        post_link_alertas_consular_page = link_alertas_consular.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_link_alertas_consular_page = link_alertas_consular.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_link_alertas_consular_page = link_alertas_consular.find("div", {"id" : "parent-fieldname-text"}).text
        list_links_alertas_consular_page = []
        links_alertas_consular_page = link_alertas_consular.find("div", {"id":"parent-fieldname-text"}).find_all("a")
        for a_alertas_consular in links_alertas_consular_page:
            list_links_alertas_consular_page.append(a_alertas_consular["href"]) 


def noticias_consular(): # check
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/noticias/colecao-de-noticias"
    mre_page = page_access(url)
    title_noticias_consular = mre_page.find("h1", class_="documentFirstHeading").text
    post_noticias_consular = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_noticias_consular = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_noticias_consular = mre_page.find("div", {"id":"content-core"}).find_all("article")
    for article_noticias_consular in content_noticias_consular:
        link_noticias_consular = page_access(article_noticias_consular.div.h2.a["href"]) 
        title_link_noticias_consular_page = link_noticias_consular.find("h1", class_="documentFirstHeading").text
        post_link_noticias_consular_page = link_noticias_consular.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_link_noticias_consular_page = link_noticias_consular.find("span", class_="documentModified").find("span", class_="value").text
        except:
            pass
        content_link_noticias_consular_page = link_noticias_consular.find("div", {"id" : "parent-fieldname-text"}).text
        list_links_noticias_consular_page = []
        links_noticias_consular_page = link_noticias_consular.find("div", {"id":"parent-fieldname-text"}).find_all("a")
        for a_noticias_consular in links_noticias_consular_page:
            link = a_noticias_consular["href"]
            pdf = link.split(".")
            if pdf[-1] == "pdf":
                list_links_noticias_consular_page.append(a_noticias_consular["href"])


def infos_classificadas(): # check
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/informacoes-classificadas"
    mre_page = page_access(url)
    title_infos_classificadas = mre_page.find("h1", class_="documentFirstHeading").text
    post_infos_classificadas = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos_classificadas = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_infos_classificadas = mre_page.find("div", {"id":"content-core"}).find_all("ol")
    for ol_infos_classificadas in content_infos_classificadas:
        ol_li_infos_classificadas = ol_infos_classificadas.find_all("li")
        for li_infos_classificadas in content_infos_classificadas:
            link_infos_classificadas = page_access(li_infos_classificadas.p.a["href"]) 
            title_link_infos_classificadas = link_infos_classificadas.find("h1", class_="documentFirstHeading").text
            post_link_infos_classificadas = link_infos_classificadas.find("span", class_="documentPublished").find("span", class_="value").text
            try:
                update_link_infos_classificadas = link_infos_classificadas.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            list_links_infos_classificadas = [] 
            links_infos_classificadas = link_infos_classificadas.find("div", {"id":"parent-fieldname-text"}).find_all("a")
            for a_infos_classificadas in links_infos_classificadas:
                list_links_infos_classificadas.append(a_infos_classificadas["href"])
        

def dados_abertos(): # ajustar erros - fix it later
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/dados-abertos"
    mre_page = page_access(url)
    title_dados_abertos = mre_page.find("h1", class_="documentFirstHeading").text
    post_dados_abertos = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados_abertos = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_dados_abertos = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_dados_abertos in content_dados_abertos:
        link_dados_abertos = page_access(a_dados_abertos["href"]) 
        try:
            title_link_dados_abertos_page = link_dados_abertos.find("h1", class_="documentFirstHeading").text
        except:
            print("sem título")
        try: 
            post_link_dados_abertos_page = link_dados_abertos.find("span", class_="documentPublished").find("span", class_="value").text
        except:
            print("sem post")
        try:
            update_link_dados_abertos_page = link_dados_abertos.find("span", class_="documentModified").find("span", class_="value").text
        except:
            print("sem update")
        list_links_dados_abertos_page = []
        try: 
            links_dados_abertos_page = link_dados_abertos.find("div", {"id":"content-core"}).find_all("a")
            for a_dados_abertos in links_dados_abertos_page:
                list_links_dados_abertos_page.append(a_dados_abertos["href"])
            print(list_links_dados_abertos_page)
        except:
            print("sem link")
    

def cgirc(): # check
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/gestao-e-governanca/governanca/comite-de-governanca-riscos-e-controle-cgrc"
    mre_page = page_access(url)
    title_cgirc = mre_page.find("h1", class_="documentFirstHeading").text
    post_cgirc = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cgirc = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_cgirc = mre_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_cgirc = []
    links_cgirc = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cgirc in links_cgirc:
        list_links_cgirc.append(a_cgirc["href"])


def pei_mre(): # check
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/gestao-e-governanca/governanca/planejamento-estrategico-institucional-do-mre-pei-mre"
    mre_page = page_access(url)
    title_pei_mre = mre_page.find("h1", class_="documentFirstHeading").text
    post_pei_mre = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_pei_mre = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    content_pei_mre = mre_page.find("div", {"id" : "parent-fieldname-text"}).text
    list_links_pei_mre = []
    links_pei_mre = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_pei_mre in links_pei_mre:
        list_links_pei_mre.append(a_pei_mre["href"])


def entrevistas(): # in progress
    url_base = "https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/"
    subpages = ["presidente-da-republica", "vice-presidente", "ministro-das-relacoes-exteriores", "secretario-geral", "diplomatas", "outras-autoridades"]
    for pages in subpages:
        url = url_base + pages
        print(url)
        if url[1]:
            url_presidente = url + "/presidente-da-republica-federativa-do-brasil-"
            print(url_presidente)
            sub = ["discursos", "artigos", "entrevistas"]
            #for subs in sub:
                #teste = url_presidente + sub
                #print(teste)
        # mre_page = page_access(url)
        # title_boletins = sd_page.find("h1", class_="documentFirstHeading").text

# https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/presidente-da-republica/presidente-da-republica-federativa-do-brasil-discursos


def resenhas_peb():
    url = "https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/resenhas-de-politica-exterior-do-brasil"
    mre_page = page_access(url)


def ocde_boletins():
    url = "https://www.gov.br/mre/pt-br/assuntos/politica-externa-comercial-e-economica/organizacoes-economicas-internacionais/brasil-na-ocde-boletim-informativo"
    mre_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/mre/pt-br/"
    bs = page_access(url) 
    # mre_noticias = noticias()
    # mre_estudos_mercado_tecnologia = estudos_mercado_tecnologia()
    # mre_alertas_consular = alertas_consular()
    # mre_noticias_consular = noticias_consular()
    # mre_infos_classificadas = infos_classificadas()
    # mre_dados_abertos = dados_abertos()
    # mre_cgirc = cgirc()
    # mre_pei_mre = pei_mre()
    mre_entrevistas = entrevistas()
    mre_resenhas_peb = resenhas_peb()
    mre_ocde_boletins = ocde_boletins()


if __name__ == "__main__":
    main()