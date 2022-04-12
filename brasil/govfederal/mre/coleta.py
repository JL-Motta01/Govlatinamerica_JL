from urllib.request import urlopen
from bs4 import BeautifulSoup


def acessar_pagina(url):
    html = urlopen(url)  
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mre/pt-br/assuntos/noticias/o-brasil-no-mundo"
    pass


def estudos_mercado_tecnologia(): # check!
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
    print("ESTUDOS MERCADO:")
    print(title_estudos_mercado_tecnologia)
    print(list_links_estudos_mercado_tecnologia)


def alertas_consular(): # check - ajustar links coletados
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/alertas/alertas"
    mre_page = page_access(url)
    title_alertas_consular = mre_page.find("h1", class_="documentFirstHeading").text
    post_alertas_consular = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_alertas_consular = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    print("ALERTAS CONSULAR:")
    print(title_alertas_consular)
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
        print(list_links_alertas_consular_page)


def noticias_consular(): # check - conferir listas vazias
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/noticias/colecao-de-noticias"
    mre_page = page_access(url)
    title_noticias_consular = mre_page.find("h1", class_="documentFirstHeading").text
    post_noticias_consular = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_noticias_consular = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    print("NOTÍCIAS CONSULAR:")
    print(title_noticias_consular)
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
        print(list_links_noticias_consular_page)


def infos_classificadas(): # check!
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/informacoes-classificadas"
    mre_page = page_access(url)
    title_infos_classificadas = mre_page.find("h1", class_="documentFirstHeading").text
    post_infos_classificadas = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_infos_classificadas = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    print("INFOS CLASSIFICADAS:")
    print(title_infos_classificadas)
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
            print(list_links_infos_classificadas)
        

def dados_abertos(): # ajustar erros - fix it later
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/dados-abertos"
    mre_page = page_access(url)
    title_dados_abertos = mre_page.find("h1", class_="documentFirstHeading").text
    post_dados_abertos = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados_abertos = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    list_pages_dados_abertos = []
    list_pdfs_dados_abertos = []
    try: 
        content_dados_abertos = mre_page.find("div", {"id":"content-core"}).find_all("a")
        for a_dados_abertos in content_dados_abertos:
            list_pages_dados_abertos.append(a_dados_abertos["href"])
        del list_pages_dados_abertos[-1]
        del list_pages_dados_abertos[-1]
    except:
        pass
    print(list_pages_dados_abertos)

    """
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
    """


def cgirc(): # check!
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
    print("CGIRC:")
    print(title_cgirc)
    print(list_links_cgirc)


def pei_mre(): # check!
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
    print("PEI MRE:")
    print(title_pei_mre)
    print(list_links_pei_mre)


def publicacoes_cargos(): # in progress - fix it later
    url_base = "https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas/"
    subpages = ["outras-autoridades/"]
    # ["presidente-da-republica/presidente-da-republica-federativa-do-brasil-", "vice-presidente/", "ministro-das-relacoes-exteriores/", "secretario-geral/", "diplomatas/", "outras-autoridades/"]
    for pages in subpages:
        montagem_url = url_base + pages
        sub = ["discursos", "artigos", "entrevistas"]
        for subs in sub:
            url = montagem_url + subs
            try: 
                mre_page = page_access(url)
                print(f'URL: {url} / ACESSOU')
                title_publicacoes_cargos = mre_page.find("h1", class_="documentFirstHeading").text
                post_publicacoes_cargos = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
                try:
                    update_publicacoes_cargos = mre_page.find("span", class_="documentModified").find("span", class_="value").text
                except:
                    pass
                try:
                    counter = 0 
                    list_url_publicacoes_cargos = []
                    while counter < 391:
                        domain = url + "?b_start:int="
                        domain += str(counter) 
                        counter += 30
                        list_url_publicacoes_cargos.append(domain)
                    print(f'GERANDO OS HTMLS: {list_url_publicacoes_cargos}')
                    for url_publicacoes_cargos in list_url_publicacoes_cargos:
                        page = page_access(url_publicacoes_cargos)
                        content_publicacoes_cargos = page.find("div", {"id":"content-core"}).find_all("article")
                        for article_publicacoes_cargos in content_publicacoes_cargos:
                            link_publicacoes_cargos = page_access(article_publicacoes_cargos.div.h2.a["href"]) 
                            # entrando
                            title_link_publicacoes_cargos = link_publicacoes_cargos.find("h1", class_="documentFirstHeading").text
                            print("ACESSOU O WHILE")
                            print(f'TÍTULO: {title_link_publicacoes_cargos}')
                            try:
                                post_link_publicacoes_cargos = link_publicacoes_cargos.find("span", class_="documentPublished").find("span", class_="value").text
                                print(f'DATA POST: {post_link_publicacoes_cargos}')
                            except:
                                post_link_publicacoes_cargos = "NA"
                                print(f'DATA POST: {post_link_publicacoes_cargos}')
                            try:
                                update_link_publicacoes_cargos = link_publicacoes_cargos.find("span", class_="documentModified").find("span", class_="value").text
                                print(f'DATA ATUALIZAÇÃO: {update_link_publicacoes_cargos}')
                            except:
                                update_link_publicacoes_cargos = "NA"
                                print(f'DATA ATUALIZAÇÃO: {update_link_publicacoes_cargos}')
                            content_link_publicacoes_cargos = link_publicacoes_cargos.find("div", {"id":"parent-fieldname-text"}).text
                            print(f'CONTEÚDO: {content_link_publicacoes_cargos}')
                            lista_tags_publicacoes_cargos = []
                            try: 
                                tags_publicacoes_cargos = link_publicacoes_cargos.find("div", {"id":"category"}).find_all("span")
                                for span_publicacoes_cargos in tags_publicacoes_cargos:
                                    lista_tags_publicacoes_cargos.append(span_publicacoes_cargos.text)
                            except:
                                lista_tags_publicacoes_cargos.append("notícia sem tag")
                            if lista_tags_publicacoes_cargos[0] != 'notícia sem tag' :
                                del lista_tags_publicacoes_cargos[0]
                            print(f'TAGS: {lista_tags_publicacoes_cargos}')
                except:
                    content_publicacoes_cargos = mre_page.find("div", {"id":"content-core"}).find_all("article")
                    for article_publicacoes_cargos in content_publicacoes_cargos:
                        link_publicacoes_cargos = page_access(article_publicacoes_cargos.div.h2.a["href"]) 
                        # entrando
                        title_link_publicacoes_cargos = link_publicacoes_cargos.find("h1", class_="documentFirstHeading").text
                        print("ACESSOU O URL NORMAL")
                        print(title_link_publicacoes_cargos)
                    """
                    content_publicacoes_cargos = page.find("div", {"id":"content-core"}).find_all("article")
                    for article_publicacoes_cargos in content_publicacoes_cargos:
                        link_publicacoes_cargos = page_access(article_publicacoes_cargos.div.h2.a["href"]) 
                        # entrando
                        title_link_publicacoes_cargos = link_publicacoes_cargos.find("h1", class_="documentFirstHeading").text
                        try:
                            post_link_publicacoes_cargos = link_publicacoes_cargos.find("span", class_="documentPublished").find("span", class_="value").text
                        except:
                            pass
                        try:
                            update_link_publicacoes_cargos = link_publicacoes_cargos.find("span", class_="documentModified").find("span", class_="value").text
                        except:
                            pass
                        content_link_publicacoes_cargos = link_publicacoes_cargos.find("div", {"id":"parent-fieldname-text"}).text
                        lista_tags_publicacoes_cargos = []
                        try: 
                            tags_publicacoes_cargos = link_publicacoes_cargos.find("div", {"id":"category"}).find_all("span")
                            for span_publicacoes_cargos in tags_publicacoes_cargos:
                                lista_tags_publicacoes_cargos.append(span_publicacoes_cargos.text)
                        except:
                            lista_tags_publicacoes_cargos.append("notícia sem tag")
                        if lista_tags_publicacoes_cargos[0] != 'notícia sem tag' :
                            del lista_tags_publicacoes_cargos[0]
                    """
            except:
                url_minis_re = url + "-mre"
                mre_page = page_access(url_minis_re)
                print(f'URL MINIS. REX.: {url_minis_re} / ACESSOU')
                title_publicacoes_cargos = mre_page.find("h1", class_="documentFirstHeading").text
                post_publicacoes_cargos = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
                try:
                    update_publicacoes_cargos = mre_page.find("span", class_="documentModified").find("span", class_="value").text
                except:
                    pass
            """
            mre_page = page_access(url)
            title_publicacoes_cargos = mre_page.find("h1", class_="documentFirstHeading").text
            post_publicacoes_cargos = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
            update_publicacoes_cargos = mre_page.find("span", class_="documentModified").find("span", class_="value").text
            print(title_publicacoes_cargos, post_publicacoes_cargos, update_publicacoes_cargos)
            """


def resenhas_peb(): # check!
    url = "https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/resenhas-de-politica-exterior-do-brasil"
    mre_page = page_access(url)
    title_resenhas_peb = mre_page.find("h1", class_="documentFirstHeading").text
    post_resenhas_peb = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_resenhas_peb = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    list_links_resenhas_peb = []
    links_resenhas_peb = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_resenhas_peb in links_resenhas_peb:
        link = a_resenhas_peb["href"]
        pdf = link.split(".")
        if pdf[-1] == "pdf":
            list_links_resenhas_peb.append(a_resenhas_peb["href"])
    print("RESENHAS PEB:")
    print(title_resenhas_peb)
    print(list_links_resenhas_peb)


def ocde_boletins(): # check!
    url = "https://www.gov.br/mre/pt-br/assuntos/politica-externa-comercial-e-economica/organizacoes-economicas-internacionais/brasil-na-ocde-boletim-informativo"
    mre_page = page_access(url)
    title_ocde_boletins = mre_page.find("h1", class_="documentFirstHeading").text
    post_ocde_boletins = mre_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_ocde_boletins = mre_page.find("span", class_="documentModified").find("span", class_="value").text
    list_links_ocde_boletins = []
    links_ocde_boletins = mre_page.find("div", {"id":"content-core"}).find_all("a")
    for a_ocde_boletins in links_ocde_boletins:
        link = a_ocde_boletins["href"]
        pdf = link.split(".")
        if pdf[-1] == "pdf":
            list_links_ocde_boletins.append(a_ocde_boletins["href"])
    print("OCDE BOLETINS:")
    print(title_ocde_boletins)
    print(list_links_ocde_boletins)


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
    mre_publicacoes_cargos = publicacoes_cargos()
    # mre_resenhas_peb = resenhas_peb()
    # mre_ocde_boletins = ocde_boletins()


if __name__ == "__main__":
    main()