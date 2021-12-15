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


def entregas(): # in progress - FIX IT LATER: entrar nas páginas corretamente
    url_2021 = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/entregas/2021?b_size=60"
    url_2020 = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/entregas/2020?b_size=60"
    url_2019 = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/entregas/2019?b_size=60"
    list_url_entregas = []
    list_links_entregas = []
    list_url_entregas.append(url_2021)
    list_url_entregas.append(url_2020)
    list_url_entregas.append(url_2019)
    if list_url_entregas[0]:
        entregas_2019 = page_access(list_url_entregas[0])
        print("2021")
        counter = 0
        while counter < 301:
            domain = url_2021 + "&b_start:int="
            domain += str(counter) 
            counter += 60
            list_links_entregas.append(domain)
        for link_entregas in list_links_entregas:
            mcti_page = page_access(link_entregas)
            links_entregas = mcti_page.find("div", {"id":"content-core"}).find_all("li")
            for li_entregas in links_entregas:
                link_entrega = page_access(li_entregas.div.h2.a["href"]) 
                title_link_entrega = link_entrega.find("h1", class_="documentFirstHeading").text
                print(title_link_entrega)
                try:
                    post_link_entrega = link_entrega.find("span", class_="documentPublished").find("span", class_="value").text
                    update_link_entrega = link_entrega.find("span", class_="documentModified").find("span", class_="value").text
                except:
                    pass
                content_link_entrega = link_entrega.find("div", {"id":"parent-fieldname-text"}).text

    """
    url_base = "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/entregas"
    anos = ["/2021?b_size=60", "/2020?b_size=60", "/2019?b_size=60"]
    for ano in anos:
        url = url_base + ano
        page = page_access(url)
        list_url_entregas = []
        try: 
            print("2021")
            counter = 0
            while counter < 301:
                domain = url + "&b_start:int="
                domain += str(counter) 
                counter += 60
                list_url_entregas.append(domain)
            for url_entregas in list_url_entregas:
                mcti_page = page_access(url_entregas)
                links_entregas = mcti_page.find("div", {"id":"content-core"}).find_all("li")
                for li_entregas in links_entregas:
                    link_entrega = page_access(li_entregas.div.h2.a["href"]) 
                    title_link_entrega = link_entrega.find("h1", class_="documentFirstHeading").text
                    print(title_link_entrega)
                    try:
                        post_link_entrega = link_entrega.find("span", class_="documentPublished").find("span", class_="value").text
                        update_link_entrega = link_entrega.find("span", class_="documentModified").find("span", class_="value").text
                    except:
                        pass
                    content_link_entrega = link_entrega.find("div", {"id":"parent-fieldname-text"}).text
        except:
            try:
                print("2020")
                counter = 0
                while counter < 61:
                    domain = url + "&b_start:int="
                    domain += str(counter) 
                    counter += 60
                    list_url_entregas.append(domain)
                for url_entregas in list_url_entregas:
                    mcti_page = page_access(url_entregas)
                    links_entregas = mcti_page.find("div", {"id":"content-core"}).find_all("li")
                for li_entregas in links_entregas:
                    link_entrega = page_access(li_entregas.div.h2.a["href"]) 
                    title_link_entrega = link_entrega.find("h1", class_="documentFirstHeading").text
                    print(title_link_entrega)
                    try:
                        post_link_entrega = link_entrega.find("span", class_="documentPublished").find("span", class_="value").text
                        update_link_entrega = link_entrega.find("span", class_="documentModified").find("span", class_="value").text
                    except:
                        pass
                    content_link_entrega = link_entrega.find("div", {"id":"parent-fieldname-text"}).text
            except:
                    print("2019")
                    links_entregas = mcti_page.find("div", {"id":"content-core"}).find_all("li")
                    for li_entregas in links_entregas:
                        link_entrega = page_access(li_entregas.div.h2.a["href"]) 
                        title_link_entrega = link_entrega.find("h1", class_="documentFirstHeading").text
                        print(title_link_entrega)
                        try:
                            post_link_entrega = link_entrega.find("span", class_="documentPublished").find("span", class_="value").text
                            update_link_entrega = link_entrega.find("span", class_="documentModified").find("span", class_="value").text
                        except:
                            pass
                        content_link_entrega = link_entrega.find("div", {"id":"parent-fieldname-text"}).text
    """

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


def informes_humanidade(): # check
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-covid-19-humanidades-mcti"
    mcti_page = page_access(url)
    title_informes_humanidade = mcti_page.find("h2", class_="outstanding-title").text
    link_informes_humanidade = mcti_page.find("div", {"id":"content"}).find_all("div", class_="nitf-basic-tile tile-content")
    for div_informes_humanidade in link_informes_humanidade:
        informes_humanidade_pages = page_access(div_informes_humanidade.h2.a["href"])
        title_informe_humanidade = informes_humanidade_pages.find("h1", class_="documentFirstHeading").text
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


def informes_economia(): # check
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-rede-clima-subrede-economia"
    mcti_page = page_access(url)
    content_informes_economia = mcti_page.find("div", class_="cover-richtext-tile tile-content").text
    list_links_informes_economia = []
    links_informes_economia = mcti_page.find("div", {"id":"content"}).find_all("a")
    for a_informes_economia in links_informes_economia:
        list_links_informes_economia.append(a_informes_economia["href"])


def informes_variante(): # check
    url = "https://www.gov.br/mcti/pt-br/coronavirus/informes-redevirus-mcti-variante-omicron"
    mcti_page = page_access(url)
    list_links_informes_variante = []
    links_informes_variante = mcti_page.find("div", {"id":"content"}).find_all("div", class_="outstanding-header tile-content")
    for div_informes_variante in links_informes_variante:
        list_links_informes_variante.append(div_informes_variante.h2.a["href"])


def infos(): # check
    url = "https://www.gov.br/mcti/pt-br/acesso-a-informacao/informacoes-classificadas"
    mcti_page = page_access(url)
    title_informes_infos = mcti_page.find("h2", class_="outstanding-title").text
    content_informes_infos = mcti_page.find("div", class_="cover-richtext-tile tile-content").text
    list_links_informes_infos = []
    links_informes_infos = mcti_page.find("div", {"id":"content"}).find_all("td", {"headers" : "download"})
    for td_informes_infos in links_informes_infos:
        list_links_informes_infos.append(td_informes_infos.a["href"])


def dados(): # check
    url = "https://www.gov.br/mcti/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-1"
    mcti_page = page_access(url)
    content_informes_dados = mcti_page.find("div", class_="cover-richtext-tile tile-content").text
    list_links_informes_dados = []
    links_informes_dados = mcti_page.find("div", class_="row linha-discreta").find_all("a")
    for a_informes_dados in links_informes_dados:
        list_links_informes_dados.append(a_informes_dados["href"])


def comunicados(): # check
    url = "https://www.gov.br/mcti/pt-br/centrais-de-conteudo/comunicados-mcti"
    mcti_page = page_access(url)
    cards_comunicados = mcti_page.find("div", class_="wrapper").find_all("div", class_="card")
    for card in cards_comunicados:
        try:
            comunicado_page = page_access(card.a["href"])
            title_comunicado = comunicado_page.find("h1", class_="documentFirstHeading").text
            post_comunicado = comunicado_page.find("span", class_="documentPublished").find("span", class_="value").text
            try:
                update_comunicado = comunicado_page.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_comunicado = comunicado_page.find("div", {"id" : "parent-fieldname-text"}).text
            list_links_comunicado = []
            links_comunicado = comunicado_page.find("div", {"id" : "content"}).find_all("a")
            for a_comunicado in links_comunicado:
                list_links_comunicado.append(a["href"])
        except:
            list_comunicados = []
            list_comunicados.append(card.a["href"])


def main():
    global bs
    url = "https://www.gov.br/mcti/pt-br"
    bs = page_access(url) 
    # mcti_noticias = noticias()
    # mcti_boletins = boletins()
    mcti_entregas = entregas()
    # mcti_informes_corona = informes_corona()
    # mcti_informes_previr = informes_previr()
    # mcti_informes_humanidade = informes_humanidade()
    # mcti_informes_economia = informes_economia()
    # mcti_informes_variante = informes_variante()
    # mcti_infos = infos()
    # mcti_dados = dados()
    # mcti_comunicados = comunicados()


if __name__ == "__main__":
    main()