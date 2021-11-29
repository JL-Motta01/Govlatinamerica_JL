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


def contratacoes(): # check
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/licitacoes-e-contratos/plano-anual-de-contratacoes" 
    mme_page = page_access(url)
    contratacao = mme_page.find("div", class_="wrapper").find_all("div", class_="card")  
    list_contratacoes = []  
    for card in contratacao:
        list_contratacoes.append(card.a["href"])  
    if list_contratacoes[0]: # check
        contratacoes_2022 = page_access(list_contratacoes[0])
        title_contratacoes_2022 = contratacoes_2022.find("h1", class_="documentFirstHeading").text
        post_contratacoes_2022 = contratacoes_2022.find("span", class_="documentPublished").find("span", class_="value").text
        update_contratacoes_2022 = contratacoes_2022.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contratacoes_2022 = []
        link_contratacoes_2022 = contratacoes_2022.find("div", {"id":"content-core"}).find_all("a")
        for a_contratacoes_2022 in link_contratacoes_2022:
            list_link_contratacoes_2022.append(a_contratacoes_2022["href"])
    if list_contratacoes[1]: # check
        contratacoes_2021 = page_access(list_contratacoes[1])
        title_contratacoes_2021 = contratacoes_2021.find("h1", class_="documentFirstHeading").text
        post_contratacoes_2021 = contratacoes_2021.find("span", class_="documentPublished").find("span", class_="value").text
        update_contratacoes_2021 = contratacoes_2021.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contratacoes_2021 = []
        link_contratacoes_2021 = contratacoes_2021.find("div", {"id":"content-core"}).find_all("a")
        for a_contratacoes_2021 in link_contratacoes_2021:
            list_link_contratacoes_2021.append(a_contratacoes_2021["href"])
    if list_contratacoes[2]: # check
        contratacoes_2020 = page_access(list_contratacoes[2])
        title_contratacoes_2020 = contratacoes_2020.find("h1", class_="documentFirstHeading").text
        post_contratacoes_2020 = contratacoes_2020.find("span", class_="documentPublished").find("span", class_="value").text
        update_contratacoes_2020 = contratacoes_2020.find("span", class_="documentModified").find("span", class_="value").text
        list_link_contratacoes_2020 = []
        link_contratacoes_2020 = contratacoes_2020.find("div", {"id":"content-core"}).find_all("a")
        for a_contratacoes_2020 in link_contratacoes_2020:
            list_link_contratacoes_2020.append(a_contratacoes_2020["href"])


def contratos(): # in progress - analisar
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/licitacoes-e-contratos/contratos-1" 
    mme_page = page_access(url)
    contrato = mme_page.find("div", class_="wrapper").find_all("div", class_="card")  
    list_contratos = []  
    for card in contrato:
        list_contratos.append(card.a["href"])  
    if list_contratos[0]: # in progress
        contrato_2021 = page_access(list_contratos[0])
        contrato2021 = contrato_2021.find("div", class_="wrapper").find_all("div", class_="card")  
        list_contratos_2021 = []  
        for card in contrato2021:
            list_contratos_2021.append(card.a["href"]) 
        if list_contratos_2021[0]: # check
            contrato_mme1 = page_access(list_contratos_2021[0])
            title_contrato_mme1 = contrato_mme1.find("h1", class_="documentFirstHeading").text
            post_contrato_mme1 = contrato_mme1.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme1 = contrato_mme1.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme1 = []
            link_contrato_mme1 = contrato_mme1.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme1 in link_contrato_mme1:
                list_link_contrato_mme1.append(a_contrato_mme1["href"])
        if list_contratos_2021[1]: # check
            contrato_mme2 = page_access(list_contratos_2021[1])
            title_contrato_mme2 = contrato_mme2.find("h1", class_="documentFirstHeading").text
            post_contrato_mme2 = contrato_mme2.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme2 = contrato_mme2.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme2 = []
            link_contrato_mme2 = contrato_mme2.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme2 in link_contrato_mme2:
                list_link_contrato_mme2.append(a_contrato_mme2["href"])
        if list_contratos_2021[2]: # check
            contrato_mme3 = page_access(list_contratos_2021[2])
            title_contrato_mme3 = contrato_mme3.find("h1", class_="documentFirstHeading").text
            post_contrato_mme3 = contrato_mme3.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme3 = contrato_mme3.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme3 = []
            link_contrato_mme3 = contrato_mme3.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme3 in link_contrato_mme3:
                list_link_contrato_mme3.append(a_contrato_mme3["href"])
        if list_contratos_2021[3]: # check
            contrato_mme4 = page_access(list_contratos_2021[3])
            title_contrato_mme4 = contrato_mme4.find("h1", class_="documentFirstHeading").text
            post_contrato_mme4 = contrato_mme4.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme4 = contrato_mme4.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme4 = []
            link_contrato_mme4 = contrato_mme4.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme4 in link_contrato_mme4:
                list_link_contrato_mme4.append(a_contrato_mme4["href"])
        if list_contratos_2021[4]: # check
            contrato_mme5 = page_access(list_contratos_2021[4])
            title_contrato_mme5 = contrato_mme5.find("h1", class_="documentFirstHeading").text
            post_contrato_mme5 = contrato_mme5.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme5 = contrato_mme5.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme5 = []
            link_contrato_mme5 = contrato_mme5.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme5 in link_contrato_mme5:
                list_link_contrato_mme5.append(a_contrato_mme5["href"])
        if list_contratos_2021[5]: # check
            contrato_mme6 = page_access(list_contratos_2021[5])
            title_contrato_mme6 = contrato_mme6.find("h1", class_="documentFirstHeading").text
            post_contrato_mme6 = contrato_mme6.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme6 = contrato_mme6.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme6 = []
            link_contrato_mme6 = contrato_mme6.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme6 in link_contrato_mme6:
                list_link_contrato_mme6.append(a_contrato_mme6["href"])
        if list_contratos_2021[6]: # check
            contrato_mme7 = page_access(list_contratos_2021[6])
            title_contrato_mme7 = contrato_mme7.find("h1", class_="documentFirstHeading").text
            post_contrato_mme7 = contrato_mme7.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme7 = contrato_mme7.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme7 = []
            link_contrato_mme7 = contrato_mme7.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme7 in link_contrato_mme7:
                list_link_contrato_mme7.append(a_contrato_mme7["href"])
        if list_contratos_2021[7]: # check
            contrato_mme8 = page_access(list_contratos_2021[7])
            title_contrato_mme8 = contrato_mme8.find("h1", class_="documentFirstHeading").text
            post_contrato_mme8 = contrato_mme8.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme8 = contrato_mme8.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme8 = []
            link_contrato_mme8 = contrato_mme8.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme8 in link_contrato_mme8:
                list_link_contrato_mme8.append(a_contrato_mme8["href"])
        if list_contratos_2021[8]: # check
            contrato_mme9 = page_access(list_contratos_2021[8])
            title_contrato_mme9 = contrato_mme9.find("h1", class_="documentFirstHeading").text
            post_contrato_mme9 = contrato_mme9.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme9 = contrato_mme9.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme9 = []
            link_contrato_mme9 = contrato_mme9.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme9 in link_contrato_mme9:
                list_link_contrato_mme9.append(a_contrato_mme9["href"])
        if list_contratos_2021[9]: # check
            contrato_mme10 = page_access(list_contratos_2021[9])
            title_contrato_mme10 = contrato_mme10.find("h1", class_="documentFirstHeading").text
            post_contrato_mme10 = contrato_mme10.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme10 = contrato_mme10.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme10 = []
            link_contrato_mme10 = contrato_mme10.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme10 in link_contrato_mme10:
                list_link_contrato_mme10.append(a_contrato_mme10["href"])
        if list_contratos_2021[10]: # check
            contrato_mme11 = page_access(list_contratos_2021[10])
            title_contrato_mme11 = contrato_mme11.find("h1", class_="documentFirstHeading").text
            post_contrato_mme11 = contrato_mme11.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme11 = contrato_mme11.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme11 = []
            link_contrato_mme11 = contrato_mme11.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme11 in link_contrato_mme11:
                list_link_contrato_mme11.append(a_contrato_mme11["href"])
        if list_contratos_2021[11]: # check
            contrato_mme12 = page_access(list_contratos_2021[11])
            title_contrato_mme12 = contrato_mme12.find("h1", class_="documentFirstHeading").text
            post_contrato_mme12 = contrato_mme12.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme12 = contrato_mme12.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme12 = []
            link_contrato_mme12 = contrato_mme12.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme12 in link_contrato_mme12:
                list_link_contrato_mme12.append(a_contrato_mme1["href"])
        if list_contratos_2021[12]: # check
            contrato_mme13 = page_access(list_contratos_2021[12])
            title_contrato_mme13 = contrato_mme13.find("h1", class_="documentFirstHeading").text
            post_contrato_mme13 = contrato_mme13.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme13 = contrato_mme13.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme13 = []
            link_contrato_mme13 = contrato_mme13.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme13 in link_contrato_mme13:
                list_link_contrato_mme13.append(a_contrato_mme13["href"])
        if list_contratos_2021[13]: # check
            contrato_mme14 = page_access(list_contratos_2021[13])
            title_contrato_mme14 = contrato_mme14.find("h1", class_="documentFirstHeading").text
            post_contrato_mme14 = contrato_mme14.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme14 = contrato_mme14.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme14 = []
            link_contrato_mme14 = contrato_mme1.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme14 in link_contrato_mme14:
                list_link_contrato_mme14.append(a_contrato_mme14["href"])
        if list_contratos_2021[14]: # check
            contrato_mme15 = page_access(list_contratos_2021[14])
            title_contrato_mme15 = contrato_mme15.find("h1", class_="documentFirstHeading").text
            post_contrato_mme15 = contrato_mme15.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme15 = contrato_mme15.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme15 = []
            link_contrato_mme15 = contrato_mme15.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme15 in link_contrato_mme15:
                list_link_contrato_mme15.append(a_contrato_mme15["href"])
        if list_contratos_2021[15]: # check
            contrato_mme16 = page_access(list_contratos_2021[15])
            title_contrato_mme16 = contrato_mme16.find("h1", class_="documentFirstHeading").text
            post_contrato_mme16 = contrato_mme16.find("span", class_="documentPublished").find("span", class_="value").text
            update_contrato_mme16 = contrato_mme16.find("span", class_="documentModified").find("span", class_="value").text
            list_link_contrato_mme16 = []
            link_contrato_mme16 = contrato_mme16.find("div", {"id":"content-core"}).find_all("a")
            for a_contrato_mme16 in link_contrato_mme16:
                list_link_contrato_mme16.append(a_contrato_mme16["href"])


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
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/metas-de-desempenho-institucional" 
    mme_page = page_access(url)
    metasinst = mme_page.find("div", class_="wrapper").find_all("div", class_="card")  
    list_metas_inst = []  
    for card in metasinst:
        list_metas_inst.append(card.a["href"])  
    if list_metas_inst[0]: # check
        metas_inst1 = page_access(list_metas_inst[0])
        title_metas_inst1 = metas_inst1.find("h1", class_="documentFirstHeading").text
        post_metas_inst1 = metas_inst1.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst1 = metas_inst1.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst1 = []
        link_metas_inst1 = metas_inst1.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst1 in link_metas_inst1:
            list_link_metas_inst1.append(a_metas_inst1["href"])
    if list_metas_inst[1]: # check
        metas_inst2 = page_access(list_metas_inst[1])
        title_metas_inst2 = metas_inst2.find("h1", class_="documentFirstHeading").text
        post_metas_inst2 = metas_inst2.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst2 = metas_inst2.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst2 = []
        link_metas_inst2 = metas_inst2.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst2 in link_metas_inst2:
            list_link_metas_inst2.append(a_metas_inst2["href"])
    if list_metas_inst[2]: # check
        metas_inst3 = page_access(list_metas_inst[2])
        title_metas_inst3 = metas_inst3.find("h1", class_="documentFirstHeading").text
        post_metas_inst3 = metas_inst3.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst3 = metas_inst3.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst3 = []
        link_metas_inst3 = metas_inst3.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst3 in link_metas_inst3:
            list_link_metas_inst3.append(a_metas_inst3["href"])
    if list_metas_inst[3]: # check
        metas_inst4 = page_access(list_metas_inst[3])
        title_metas_inst4 = metas_inst4.find("h1", class_="documentFirstHeading").text
        post_metas_inst4 = metas_inst4.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst4 = metas_inst4.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst4 = []
        link_metas_inst4 = metas_inst4.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst4 in link_metas_inst4:
            list_link_metas_inst4.append(a_metas_inst4["href"])
    if list_metas_inst[4]: # check
        metas_inst5 = page_access(list_metas_inst[4])
        title_metas_inst5 = metas_inst5.find("h1", class_="documentFirstHeading").text
        post_metas_inst5 = metas_inst5.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst5 = metas_inst5.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst5 = []
        link_metas_inst5 = metas_inst5.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst5 in link_metas_inst5:
            list_link_metas_inst5.append(a_metas_inst5["href"])
    if list_metas_inst[5]: # check
        metas_inst6 = page_access(list_metas_inst[5])
        title_metas_inst6 = metas_inst6.find("h1", class_="documentFirstHeading").text
        post_metas_inst6 = metas_inst6.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst6 = metas_inst6.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst6 = []
        link_metas_inst6 = metas_inst6.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst6 in link_metas_inst6:
            list_link_metas_inst6.append(a_metas_inst6["href"])
    if list_metas_inst[6]: # check
        metas_inst7 = page_access(list_metas_inst[6])
        title_metas_inst7 = metas_inst7.find("h1", class_="documentFirstHeading").text
        post_metas_inst7 = metas_inst7.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst7 = metas_inst7.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst7 = []
        link_metas_inst7 = metas_inst7.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst7 in link_metas_inst7:
            list_link_metas_inst7.append(a_metas_inst7["href"])
    if list_metas_inst[7]: # check
        metas_inst8 = page_access(list_metas_inst[7])
        title_metas_inst8 = metas_inst8.find("h1", class_="documentFirstHeading").text
        post_metas_inst8 = metas_inst8.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst8 = metas_inst8.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst8 = []
        link_metas_inst8 = metas_inst8.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst8 in link_metas_inst8:
            list_link_metas_inst8.append(a_metas_inst8["href"])
    if list_metas_inst[8]: # check
        metas_inst9 = page_access(list_metas_inst[8])
        title_metas_inst9 = metas_inst9.find("h1", class_="documentFirstHeading").text
        post_metas_inst9 = metas_inst9.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst9 = metas_inst9.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst9 = []
        link_metas_inst9 = metas_inst9.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst9 in link_metas_inst9:
            list_link_metas_inst9.append(a_metas_inst9["href"])
    if list_metas_inst[9]: # check
        metas_inst10 = page_access(list_metas_inst[9])
        title_metas_inst10 = metas_inst10.find("h1", class_="documentFirstHeading").text
        post_metas_inst10 = metas_inst10.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst10 = metas_inst10.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst10 = []
        link_metas_inst10 = metas_inst10.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst10 in link_metas_inst10:
            list_link_metas_inst10.append(a_metas_inst10["href"])
    if list_metas_inst[10]: # check
        metas_inst11 = page_access(list_metas_inst[10])
        title_metas_inst11 = metas_inst11.find("h1", class_="documentFirstHeading").text
        post_metas_inst11 = metas_inst11.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst11 = metas_inst11.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst11 = []
        link_metas_inst11 = metas_inst11.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst11 in link_metas_inst11:
            list_link_metas_inst11.append(a_metas_inst11["href"])
    if list_metas_inst[11]: # check
        metas_inst12 = page_access(list_metas_inst[11])
        title_metas_inst12 = metas_inst12.find("h1", class_="documentFirstHeading").text
        post_metas_inst12 = metas_inst12.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_inst12 = metas_inst12.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_inst12 = []
        link_metas_inst12 = metas_inst12.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_inst12 in link_metas_inst12:
            list_link_metas_inst12.append(a_metas_inst12["href"])  
    if list_metas_inst[12]: # check
        metas_atos = page_access(list_metas_inst[12])
        title_metas_atos = metas_atos.find("h1", class_="documentFirstHeading").text
        post_metas_atos = metas_atos.find("span", class_="documentPublished").find("span", class_="value").text
        update_metas_atos = metas_atos.find("span", class_="documentModified").find("span", class_="value").text
        list_link_metas_atos = []
        link_metas_atos = metas_atos.find("div", {"id":"content-core"}).find_all("a")
        for a_metas_atos in link_metas_atos:
            list_link_metas_atos.append(a_metas_atos["href"]) 
 

def discursos(): # check - conferir a partir de cima
    url = "https://www.gov.br/mme/pt-br/centrais-de-conteudo/publicacoes/discursos-do-ministro" 
    mme_page = page_access(url)
    discurso = mme_page.find("div", class_="tabs-content").find_all("div")  
    list_discursos = []  
    for divs_discursos in discurso:
        list_discursos.append(divs_discursos["data-url"]) 
    if list_discursos[0]: # check
        discursos_2021 = page_access(list_discursos[0])
        list_links_discursos_2021 = []
        links_discursos_2021 = discursos_2021.find("tbody").find_all("a")
        for a_discursos_2021 in links_discursos_2021:
            list_links_discursos_2021.append(a_discursos_2021["href"])
    if list_discursos[1]: # check
        discursos_2020 = page_access(list_discursos[1])
        list_links_discursos_2020 = []
        links_discursos_2020 = discursos_2020.find("tbody").find_all("a")
        for a_discursos_2020 in links_discursos_2020:
            list_links_discursos_2020.append(a_discursos_2020["href"])
    if list_discursos[2]: # check
        discursos_2019 = page_access(list_discursos[2])
        list_links_discursos_2019 = []
        links_discursos_2019 = discursos_2019.find("tbody").find_all("a")
        for a_discursos_2019 in links_discursos_2019:
            list_links_discursos_2019.append(a_discursos_2019["href"])


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


def boletins_mensais(): # in progress
    url = "https://www.gov.br/mme/pt-br/assuntos/secretarias/spe/publicacoes/boletins-mensais-de-energia" 
    mme_page = page_access(url)
    boletinsmensais = mme_page.find("div", class_="wrapper").find_all("div", class_="card")  
    list_boletins_mensais = []  
    for card_boletins_mensais in boletinsmensais:
        list_boletins_mensais.append(card_boletins_mensais.a["href"]) 
    if list_boletins_mensais[0]: # check
        boletins_2021 = page_access(list_boletins_mensais[0])
        post_boletins_2021 = boletins_2021.find("span", class_="documentPublished").find("span", class_="value").text
        update_boletins_2021 = boletins_2021.find("span", class_="documentModified").find("span", class_="value").text
        """
        list_links_boletins_2021 = []
        links_boletins_2021 = boletins_2021.find("div", class_="entries").find_all("article", class_="entry")
        for article_boletins_2021 in links_boletins_2021:
            list_links_boletins_2021.append(article_boletins_2021.span.a["href"])
        """


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
    # mme_contasanuais = contasanuais()
    # mme_contratacoes = contratacoes()
    # mme_contratos = contratos()
    # mme_luz_amaz = luz_amaz()
    # mme_metas_inst = metas_inst()
    # mme_discursos = discursos()
    # mme_apresentacoes = apresentacoes()
    # mme_boletins_covid = boletins_covid()
    # mme_informativo = informativo()
    mme_boletins_mensais = boletins_mensais()
    # mme_resenha = resenha()
    # mme_doc_potee = doc_potee()
    # mme_doc_30 = doc_30()
    # mme_relatorios = relatorios()


if __name__ == "__main__":
    main()