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
        list_links_pdp21.append(a_pdp20["href"])


def contasanuais(): # check
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/auditorias/processos-de-contas-anuais" 
    mme_page = page_access(url)
    contas_anuais = mme_page.find("div", class_="wrapper").find_all("div", class_="card")  
    list_contas_anuais = []  
    for card in contas_anuais:
        list_contas_anuais.append(card.a["href"])  
    if list_contas_anuais[0]: # check
        contas_2020 = page_access(list_contas_anuais[0])
        title_contas_2020 = contas_2020.find("h1", class_="documentFirstHeading").text
        post_contas_2020 = contas_2020.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2020 = contas_2020.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2020 = []
        link_contas_2020 = contas_2020.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2020 in link_contas_2020:
            list_link_contas_2020.append(a_contas_2020["href"])
    if list_contas_anuais[1]: # check
        contas_2019 = page_access(list_contas_anuais[1])
        title_contas_2019 = contas_2019.find("h1", class_="documentFirstHeading").text
        post_contas_2019 = contas_2019.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2019 = contas_2019.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2019 = []
        link_contas_2019 = contas_2019.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2019 in link_contas_2019:
            list_link_contas_2019.append(a_contas_2019["href"])
    if list_contas_anuais[2]: # check
        contas_2018 = page_access(list_contas_anuais[2])
        title_contas_2018 = contas_2018.find("h1", class_="documentFirstHeading").text
        post_contas_2018 = contas_2018.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2018 = contas_2018.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2018 = []
        link_contas_2018 = contas_2018.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2018 in link_contas_2018:
            list_link_contas_2018.append(a_contas_2018["href"])
    if list_contas_anuais[3]: # check
        contas_2017 = page_access(list_contas_anuais[3])
        title_contas_2017 = contas_2017.find("h1", class_="documentFirstHeading").text
        post_contas_2017 = contas_2017.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2017 = contas_2017.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2017 = []
        link_contas_2017 = contas_2017.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2017 in link_contas_2017:
            list_link_contas_2017.append(a_contas_2017["href"])
    if list_contas_anuais[4]: # check
        contas_2016 = page_access(list_contas_anuais[4])
        title_contas_2016 = contas_2016.find("h1", class_="documentFirstHeading").text
        post_contas_2016 = contas_2016.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2016 = contas_2016.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2016 = []
        link_contas_2016 = contas_2016.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2016 in link_contas_2016:
            list_link_contas_2016.append(a_contas_2016["href"])
    if list_contas_anuais[5]: # check
        contas_2015 = page_access(list_contas_anuais[5])
        title_contas_2015 = contas_2015.find("h1", class_="documentFirstHeading").text
        post_contas_2015 = contas_2015.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2015 = contas_2015.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2015 = []
        link_contas_2015 = contas_2015.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2015 in link_contas_2015:
            list_link_contas_2015.append(a_contas_2015["href"])
    if list_contas_anuais[6]: # check
        contas_2014 = page_access(list_contas_anuais[6])
        title_contas_2014 = contas_2014.find("h1", class_="documentFirstHeading").text
        post_contas_2014 = contas_2014.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2014 = contas_2014.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2014 = []
        link_contas_2014 = contas_2014.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2014 in link_contas_2014:
            list_link_contas_2014.append(a_contas_2014["href"])
    if list_contas_anuais[7]: # check
        contas_2013 = page_access(list_contas_anuais[7])
        title_contas_2013 = contas_2013.find("h1", class_="documentFirstHeading").text
        post_contas_2013 = contas_2013.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2013 = contas_2013.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2013 = []
        link_contas_2013 = contas_2013.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2013 in link_contas_2013:
            list_link_contas_2013.append(a_contas_2013["href"])
    if list_contas_anuais[8]: # check
        contas_2012 = page_access(list_contas_anuais[8])
        title_contas_2012 = contas_2012.find("h1", class_="documentFirstHeading").text
        post_contas_2012 = contas_2012.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2012 = contas_2012.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2012 = []
        link_contas_2012 = contas_2012.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2012 in link_contas_2012:
            list_link_contas_2012.append(a_contas_2012["href"])
    if list_contas_anuais[9]: # check
        contas_2011 = page_access(list_contas_anuais[9])
        title_contas_2011 = contas_2011.find("h1", class_="documentFirstHeading").text
        post_contas_2011 = contas_2011.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2011 = contas_2011.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2011 = []
        link_contas_2011 = contas_2011.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2011 in link_contas_2011:
            list_link_contas_2011.append(a_contas_2011["href"])
    if list_contas_anuais[10]: # check
        contas_2010 = page_access(list_contas_anuais[10])
        title_contas_2010 = contas_2010.find("h1", class_="documentFirstHeading").text
        post_contas_2010 = contas_2010.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2010 = contas_2010.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2010 = []
        link_contas_2010 = contas_2010.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2010 in link_contas_2010:
            list_link_contas_2010.append(a_contas_2010["href"])
    if list_contas_anuais[11]: # check
        contas_2009 = page_access(list_contas_anuais[11])
        title_contas_2009 = contas_2009.find("h1", class_="documentFirstHeading").text
        post_contas_2009 = contas_2009.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2009 = contas_2009.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2009 = []
        link_contas_2009 = contas_2009.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2009 in link_contas_2009:
            list_link_contas_2009.append(a_contas_2009["href"])
    if list_contas_anuais[12]: # check
        contas_2008 = page_access(list_contas_anuais[12])
        title_contas_2008 = contas_2008.find("h1", class_="documentFirstHeading").text
        post_contas_2008 = contas_2008.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2008 = contas_2008.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2008 = []
        link_contas_2008 = contas_2008.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2008 in link_contas_2008:
            list_link_contas_2008.append(a_contas_2008["href"])
    if list_contas_anuais[13]: # check
        contas_2007 = page_access(list_contas_anuais[13])
        title_contas_2007 = contas_2007.find("h1", class_="documentFirstHeading").text
        post_contas_2007 = contas_2007.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2007 = contas_2007.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2007 = []
        link_contas_2007 = contas_2007.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2007 in link_contas_2007:
            list_link_contas_2007.append(a_contas_2007["href"])
    if list_contas_anuais[14]: # check
        contas_2006 = page_access(list_contas_anuais[14])
        title_contas_2006 = contas_2006.find("h1", class_="documentFirstHeading").text
        post_contas_2006 = contas_2006.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2006 = contas_2006.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2006 = []
        link_contas_2006 = contas_2006.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2006 in link_contas_2006:
            list_link_contas_2006.append(a_contas_2006["href"])
    if list_contas_anuais[15]: # check
        contas_2005 = page_access(list_contas_anuais[15])
        title_contas_2005 = contas_2005.find("h1", class_="documentFirstHeading").text
        post_contas_2005 = contas_2005.find("span", class_="documentPublished").find("span", class_="value").text
        update_contas_2005 = contas_2005.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contas_2005 = []
        link_contas_2005 = contas_2005.find("div", {"id":"content-core"}).find_all("a")
        for a_contas_2005 in link_contas_2005:
            list_link_contas_2005.append(a_contas_2005["href"])


def contratacoes(): # in progress
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/licitacoes-e-contratos/plano-anual-de-contratacoes" 
    mme_page = page_access(url)
    


def contratos():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/licitacoes-e-contratos/contratos-1" 
    mme_page = page_access(url)


def luz_amaz():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/dados-abertos/programas-luz-para-todos-e-mais-luz-para-amazonia" 
    mme_page = page_access(url)


def metas_inst():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/metas-de-desempenho-institucional" 
    mme_page = page_access(url)


def discursos():
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/discursos-do-ministro" 
    mme_page = page_access(url)


def apresentacoes():
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/apresentacoes-do-ministro" 
    mme_page = page_access(url)


def boletins_covid():
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/boletins-covid-19" 
    mme_page = page_access(url)


def informativo():
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/informativo-mme-em-pauta" 
    mme_page = page_access(url)


def boletins_mensais():
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/boletins-mensais-de-energia" 
    mme_page = page_access(url)


def resenha():
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/resenha-energetica-brasileira/resenhas" 
    mme_page = page_access(url)


def doc_potee():
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/plano-de-outorgas-de-transmissao-de-energia-eletrica-potee/documentos" 
    mme_page = page_access(url)


def doc_30():
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/plano-nacional-de-energia-2030/documentos" 
    mme_page = page_access(url)


def relatorios():
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/estudos-do-pne-2050/02-relatorios-epe" 
    mme_page = page_access(url)


def main():
    global bs
    url = "https://www.gov.br/mme/pt-br"
    bs = page_access(url) 
    # mme_noticias = noticias()
    # mme_pdp21 = pdp21()
    # mme_pdp20 = pdp20()
    mme_contasanuais = contasanuais()
    # mme_contratacoes = contratacoes()
    # mme_contratos = contratos()
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