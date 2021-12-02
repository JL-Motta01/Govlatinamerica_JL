from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias(): # check
    url = "https://www.gov.br/mme/pt-br/assuntos/noticias" 
    mme_page = page_access(url)
    # título
    title_noticias = mme_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_noticias = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    counter = 0 
    list_url_noticias = []
    while counter < 3001:
        domain = "https://www.gov.br/mme/pt-br/assuntos/noticias?b_size=60&b_start:int="
        domain += str(counter) 
        counter += 60
        list_url_noticias.append(domain)
    for url_noticias in list_url_noticias:
        page = page_access(url_noticias)
        # conteúdo
        content_noticias = page.find("div", {"id":"content-core"}).find_all("li")
        for li_noticias in content_noticias:
            link_noticias = page_access(li_noticias.div.h2.a["href"]) 
            # entrando
            title_link_noticias = link_noticias.find("h1", class_="documentFirstHeading").text
            post_link_noticias = link_noticias.find("span", class_="documentPublished").find("span", class_="value").text
            try:
                update_link_noticias = link_noticias.find("span", class_="documentModified").find("span", class_="value").text
            except:
                pass
            content_link_noticias = link_noticias.find("div", {"id":"parent-fieldname-text"}).text
            # tags notícias
            lista_tags_noticias = []
            try: 
                tags_noticias = link_noticias.find("div", {"id":"category"}).find_all("span")
                for span_noticias in tags_noticias:
                    lista_tags_noticias.append(span_noticias.text)
            except:
                lista_tags_noticias.append("notícia sem tag")
            if lista_tags_noticias[0] != 'notícia sem tag' :
                del lista_tags_noticias[0]


def pdp21(): # check
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/institucional/acoes-de-desenvolvimento-de-pessoas/plano-de-desenvolvimento-de-pessoas-2013-pdp-mme-2021" 
    mme_page = page_access(url)
    title_pdp21 = mme_page.find("h1", class_="documentFirstHeading").text
    post_pdp21 = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_pdp21 = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_pdp21 = mme_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_pdp21 = []
    links_pdp21 = mme_page.find("div", {"id":"content-core"}).find_all("a")
    for a_pdp21 in links_pdp21:
        list_links_pdp21.append(a_pdp21["href"])


def pdp20(): # check
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/institucional/acoes-de-desenvolvimento-de-pessoas/plano-de-desenvolvimento-de-pessoas-2013-pdp-mme-2020" 
    mme_page = page_access(url)
    title_pdp20 = mme_page.find("h1", class_="documentFirstHeading").text
    post_pdp20 = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_pdp20 = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_pdp20 = mme_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_pdp20 = []
    links_pdp20 = mme_page.find("div", {"id":"content-core"}).find_all("a")
    for a_pdp20 in links_pdp20:
        list_links_pdp20.append(a_pdp20["href"])


def contasanuais(): # check
    url_base = "https://www.gov.br/mme/pt-br/acesso-a-informacao/auditorias/processos-de-contas-anuais/processos-de-contas-" 
    anos = ["anual-2020", "anuais-2019", "anuais-2018", "anuais-2017", "anuais-2016", "anuais-2015", "anuais-2014", "anuais-2013", "anuais-2012", "anuais-2011", "anuais-2010", "anuais-2009", "anuais-2008", "anuais-2007", "anuais-2006-1", "anuais-2005-1"]
    for ano in anos:
        url = url_base + ano
        mme_page = page_access(url)
        title_contasanuais = mme_page.find("h1", class_="documentFirstHeading").text
        post_contasanuais = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
        try:
            update_contasanuais = mme_page.find("span", class_="documentModified").find("span", class_="value").text
        except:
            print("Sem atualizações")
        try:
            content_contasanuais = mme_page.find("div", {"id" : "parent-fieldname-text"}).text
        except:
            print("Sem conteúdo")
        list_links_contasanuais = []
        links_contasanuais = mme_page.find("div", {"id":"content-core"}).find_all("a")
        for a_contasanuais in links_contasanuais:
            list_links_contasanuais.append(a_contasanuais["href"])


def contratacoes(): # check 
    url_base = "https://www.gov.br/mme/pt-br/acesso-a-informacao/licitacoes-e-contratos/plano-anual-de-contratacoes/" 
    anos = ["2022", "2021", "2020"]
    for ano in anos:
        url = url_base + ano
        mme_page = page_access(url)
        title_contratacoes = mme_page.find("h1", class_="documentFirstHeading").text
        post_contratacoes = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_contratacoes = mme_page.find("span", class_="documentModified").find("span", class_="value").text
        link_contratacoes = mme_page.find("div", {"id":"content-core"}).find_all("a")
        for a_contratacoes in link_contratacoes:
            contratacoes_pages = page_access(a_contratacoes["href"])
            link_contratacoes_pages = contratacoes_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_contratacoes = []
            for a_contratacoes_pages in link_contratacoes_pages:
                list_link_contratacoes.append(a_contratacoes_pages["href"])
    

def luz_amaz(): # check
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/dados-abertos/programas-luz-para-todos-e-mais-luz-para-amazonia" 
    mme_page = page_access(url)
    title_luz_amaz = mme_page.find("h1", class_="documentFirstHeading").text
    post_luz_amaz = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_luz_amaz = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_luz_amaz = mme_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_luz_amaz = []
    links_luz_amaz = mme_page.find("div", {"id":"content-core"}).find_all("a")
    for a_luz_amaz in links_luz_amaz:
        list_links_luz_amaz.append(a_luz_amaz["href"])


def metas_inst(): # check
    url_base = "https://www.gov.br/mme/pt-br/acesso-a-informacao/metas-de-desempenho-institucional/" 
    ciclos = ["01deg-ciclo", "02deg-ciclo", "03deg-ciclo", "04deg-ciclo", "05deg-ciclo", "06deg-ciclo", "07deg-ciclo", "08deg-ciclo", "09deg-ciclo", "10deg-ciclo", "11deg-ciclo", "12deg-ciclo", "atos-normativos-relevantes"]
    for ciclo in ciclos:
        url = url_base + ciclo
        mme_page = page_access(url)
        title_metas_inst = mme_page.find("h1", class_="documentFirstHeading").text
        post_metas_inst = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst = mme_page.find("span", class_="documentModified").find("span", class_="value").text
        link_metas_inst = mme_page.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst in link_metas_inst:
            metas_inst_pages = page_access(a_metas_inst["href"])
            link_metas_inst_pages = metas_inst_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_metas_inst = []
            for a_metas_inst_pages in link_metas_inst_pages:
                list_link_metas_inst.append(a_metas_inst_pages["href"]) 
 

def discursos(): # check  
    url_base = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/discursos-do-ministro" 
    mme_page = page_access(url_base)
    # infos gerais da página
    title_discursos = mme_page.find("h1", class_="documentFirstHeading").text
    post_discursos = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_discursos = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    # entrando nas subpáginas
    anos = ["/2021", "/2020", "/2019"]
    for ano in anos:
        url = url_base + ano
        mme_pages = page_access(url)
        list_links_discursos = []
        links_discursos = mme_pages.find("div", {"id" : "content-core"}).find_all("a")
        for a_discursos in links_discursos:
            list_links_discursos.append(a_discursos["href"])
        remove_base = "http://antigo.mme.gov.br/web/guest/comunicacao/discursos-do-ministro#collapse-"
        remove_years = ["2020-2", "2020-4", "2020-6", "2020-7", "2020-8", "2020-9", "2020-10", "2020-11", "2019-0", "2019-1", "2019-2", "2019-3", "2019-4", "2019-5", "2019-6", "2019-7", "2019-8", "2019-9", "2019-10", "2019-11"]
        for removes in remove_years:
            remove_link = remove_base + removes
            while remove_link in list_links_discursos:
                list_links_discursos.remove(remove_link)


def apresentacoes(): # check
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/apresentacoes-do-ministro" 
    mme_page = page_access(url)
    title_apresentacoes = mme_page.find("h1", class_="documentFirstHeading").text
    post_apresentacoes = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    content_apresentacoes = mme_page.find("div", {"id":"content-core"}).text
    # links
    list_links_apresentacoes = []
    links_apresentacoes = mme_page.find("div", {"id":"content-core"}).find_all("a")
    for a_apresentacoes in links_apresentacoes:
        list_links_apresentacoes.append(a_apresentacoes["href"])


def boletins_covid(): # check
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/boletins-covid-19" 
    mme_page = page_access(url)
    title_boletins_covid = mme_page.find("h1", class_="documentFirstHeading").text
    post_boletins_covid = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_boletins_covid = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_boletins_covid = mme_page.find("div", {"id":"content-core"}).text
    # links
    list_links_boletins_covid = []
    links_boletins_covid = mme_page.find("div", {"id":"content-core"}).find_all("a")
    for a_boletins_covid in links_boletins_covid:
        list_links_boletins_covid.append(a_boletins_covid["href"])


def informativo(): # check
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/informativo-mme-em-pauta" 
    mme_page = page_access(url)
    title_informativo = mme_page.find("h1", class_="documentFirstHeading").text
    post_informativo = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_informativo = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_informativo = mme_page.find("div", {"id":"content-core"}).text
    # links
    list_links_informativo = []
    links_informativo = mme_page.find("table", class_="plain").find_all("a")
    for a_informativo in links_informativo:
        list_links_informativo.append(a_informativo["href"])


def boletins_mensais(): # check
    url_base = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/boletins-mensais-de-energia/"
    anos = ["2021/portugues", "2010-1/portugues", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009"]
    for ano in anos:
        url = url_base + ano
        mme_page = page_access(url)
        post_boletins = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_boletins = mme_page.find("span", class_="documentModified").find("span", class_="value").text
        list_links_boletins = []
        links_boletins = mme_page.find("div", {"id" : "content-core"}).find_all("a")
        for a_boletins in links_boletins:
            list_links_boletins.append(a_boletins["href"])
        if list_links_boletins[0] == url_base + ano + "?b_start:int=20" :
            mme_page2 = page_access(list_links_boletins[0])
            links_boletins2 = mme_page2.find("tbody").find_all("a")
            for a_boletins2 in links_boletins2:
                list_links_boletins.append(a_boletins2["href"]) 
            del (list_links_boletins[0:2])
            del (list_links_boletins[20:22])
        # entra nos links
        for pages_boletins in list_links_boletins:
            boletins_pages = page_access(pages_boletins)
            link_boletins_pages = boletins_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_boletins = []
            for a_boletins_pages in link_boletins_pages:
                list_link_boletins.append(a_boletins_pages["href"])


def resenha(): # check
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/resenha-energetica-brasileira/resenhas" 
    mme_page = page_access(url)
    title_resenha = mme_page.find("h1", class_="documentFirstHeading").text
    post_resenha = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_resenha = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_resenha = mme_page.find("div", class_="has-table").text
    links_resenha = mme_page.find("tbody").find_all("a")
    for a_resenha in links_resenha:
        resenha_pages = page_access(a_resenha["href"])
        link_resenha_pages = resenha_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_resenha_pages = []
        for a_resenha_pages in link_resenha_pages:
            list_link_resenha_pages.append(a_resenha_pages["href"])


def doc_potee(): # check
    url_base = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/plano-de-outorgas-de-transmissao-de-energia-eletrica-potee/documentos/" 
    anos = ["2021", "2020", "2019", "2018", "2017", "2016", "2015"]
    for ano in anos:
        url = url_base + ano
        mme_page = page_access(url)
        title_doc_potee = mme_page.find("h1", class_="documentFirstHeading").text
        post_doc_potee = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
        update_doc_potee = mme_page.find("span", class_="documentModified").find("span", class_="value").text
        link_doc_potee = mme_page.find("div", {"id":"content-core"}).find_all("a")
        for a_doc_potee in link_doc_potee:
            doc_potee_pages = page_access(a_doc_potee["href"])
            link_doc_potee_pages = doc_potee_pages.find("div", {"id" : "content-core"}).find_all("a")
            list_link_doc_potee = []
            for a_doc_potee_pages in link_doc_potee_pages:
                list_link_doc_potee.append(a_doc_potee_pages["href"])
    

def doc_30(): # check
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/plano-nacional-de-energia-2030/documentos" 
    mme_page = page_access(url)
    title_doc_30 = mme_page.find("h1", class_="documentFirstHeading").text
    post_doc_30 = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_doc_30 = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    content_doc_30 = mme_page.find("div", class_="has-table").text
    links_doc_30 = mme_page.find("tbody").find_all("a")
    for a_doc_30 in links_doc_30:
        doc_30_pages = page_access(a_doc_30["href"])
        link_doc_30_pages = doc_30_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_doc_30_pages = []
        for a_doc_30_pages in link_doc_30_pages:
            list_link_doc_30_pages.append(a_doc_30_pages["href"])


def relatorios(): # check
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/estudos-do-pne-2050/02-relatorios-epe" 
    mme_page = page_access(url)
    title_relatorios = mme_page.find("h1", class_="documentFirstHeading").text
    post_relatorios = mme_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_relatorios = mme_page.find("span", class_="documentModified").find("span", class_="value").text
    list_links_relatorios = []
    links_relatorios = mme_page.find("div", {"id" : "content-core"}).find_all("a")
    for a_relatorios in links_relatorios:
        list_links_relatorios.append(a_relatorios["href"])
    if list_links_relatorios[0] == url + "?b_start:int=20" :
        mme_page2 = page_access(list_links_relatorios[0])
        links_relatorios2 = mme_page2.find("tbody").find_all("a")
        for a_relatorios2 in links_relatorios2:
            list_links_relatorios.append(a_relatorios2["href"])
        del (list_links_relatorios[0:2])
        del (list_links_relatorios[20:22])
    # entra nos links
    for pages_relatorios in list_links_relatorios:
        relatorios_pages = page_access(pages_relatorios)
        link_relatorios_pages = relatorios_pages.find("div", {"id" : "content-core"}).find_all("a")
        list_link_relatorios = []
        for a_relatorios_pages in link_relatorios_pages:
            list_link_relatorios.append(a_relatorios_pages["href"])


def main():
    global bs
    url = "https://www.gov.br/mme/pt-br"
    bs = page_access(url) 
    # mme_noticias = noticias()
    # mme_pdp21 = pdp21()
    # mme_pdp20 = pdp20()
    mme_contasanuais = contasanuais()
    # mme_contratacoes = contratacoes()
    # mme_luz_amaz = luz_amaz()
    # mme_metas_inst = metas_inst()
    # mme_discursos = discursos()
    # mme_apresentacoes = apresentacoes()
    # mme_boletins_covid = boletins_covid()
    # mme_informativo = informativo()
    # mme_boletins_mensais = boletins_mensais()
    # mme_resenha = resenha()
    # mme_doc_potee = doc_potee()
    # mme_doc_30 = doc_30()
    # mme_relatorios = relatorios()


if __name__ == "__main__":
    main()