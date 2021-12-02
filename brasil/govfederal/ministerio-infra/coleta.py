from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/noticias" 
    mi_page = page_access(url)
    # título
    title_noticias = mi_page.find("h1", class_="documentFirstHeading").text
    # datas
    post_noticias = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    counter = 0 
    list_url_noticias = []
    while counter < 8701:
        domain = "https://www.gov.br/infraestrutura/pt-br/assuntos/noticias?b_start:int="
        domain += str(counter) 
        counter += 30
        list_url_noticias.append(domain)
    for url_noticias in list_url_noticias:
        page = page_access(url_noticias)
        # conteúdo
        content_noticias = page.find("div", {"id":"content-core"}).find_all("article")
        for article_noticias in content_noticias:
            link_noticias = page_access(article_noticias.div.h2.a["href"]) 
            # entrando
            title_link_noticias = link_noticias.find("h1", class_="documentFirstHeading").text
            try:
                post_link_noticias = link_noticias.find("span", class_="documentPublished").find("span", class_="value").text
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


def arq_rel(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/arquivos-relatorios-orcamentarios" 
    mi_page = page_access(url)
    title_arq_rel = mi_page.find("h1", class_="documentFirstHeading").text
    post_arq_rel = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_arq_rel = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    counter = 0 
    list_url_arq_rel = []
    while counter < 61:
        domain = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/arquivos-relatorios-orcamentarios?b_start:int="
        domain += str(counter) 
        counter += 20
        list_url_arq_rel.append(domain)
    for url_arq_rel in list_url_arq_rel:
        page = page_access(url_arq_rel)
        # conteúdo
        content_arq_rel = page.find("div", {"id":"content-core"}).find_all("article")
        for article_arq_rel in content_arq_rel:
            link_arq_rel = page_access(article_arq_rel.a["href"]) 
            # entrando
            title_link_arq_rel = link_arq_rel.find("h1", class_="documentFirstHeading").text
            try:
                post_link_arq_rel = link_arq_rel.find("span", class_="documentPublished").find("span", class_="value").text
                update_link_arq_rel = link_arq_rel.find("span", class_="documentModified").find("span", class_="value").text
                content_link_arq_rel = link_arq_rel.find("div", {"id":"parent-fieldname-text"}).text
            except:
                pass
            # links 
            list_links_arq_rel = [] 
            try: 
                links_arq_rel = link_arq_rel.find("div", {"id":"content-core"}).find_all("a")
                for a_arq_rel in links_arq_rel:
                    list_links_arq_rel.append(a_arq_rel["href"])
            except:
                pass


def ri(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/relacoes-internacionais-portos" 
    mi_page = page_access(url)
    title_ri = mi_page.find("h1", class_="documentFirstHeading").text
    post_ri = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_ri = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_ri = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_ri = []
    links_ri = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_ri in links_ri:
        list_links_ri.append(a_ri["href"])


def planos(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/planos-mestres-portos" 
    mi_page = page_access(url)
    title_planos = mi_page.find("h1", class_="documentFirstHeading").text
    post_planos = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_planos = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_planos = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_planos = []
    links_planos = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_planos in links_planos:
        list_links_planos.append(a_planos["href"])


def rel_orc(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/relatorios-orcamentarios" 
    mi_page = page_access(url)
    title_rel_orc = mi_page.find("h1", class_="documentFirstHeading").text
    post_rel_orc = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_rel_orc = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_rel_orc = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_rel_orc = []
    links_rel_orc = mi_page.find("div", {"id":"parent-fieldname-text"}).find_all("a")
    for a_rel_orc in links_rel_orc:
        try:
            list_links_rel_orc.append(a_rel_orc["href"])
        except:
            pass


def ppa(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/plano-plurianual-2013-ppa-2020-2023-minfra" 
    mi_page = page_access(url)
    title_ppa = mi_page.find("h1", class_="documentFirstHeading").text
    post_ppa = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_ppa = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_ppa = []
    links_ppa = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_ppa in links_ppa:
        list_links_ppa.append(a_ppa["href"])


def arq_ppa(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/arquivos-plano-plurianual" 
    mi_page = page_access(url)
    title_arq_ppa = mi_page.find("h1", class_="documentFirstHeading").text
    post_arq_ppa = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_arq_ppa = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_arq_ppa = mi_page.find("div", class_="entries").text
    # links
    list_links_arq_ppa = []
    links_arq_ppa = mi_page.find("div", {"id":"content-core"}).find_all("article")
    for article_arq_ppa in links_arq_ppa:
        list_links_arq_ppa.append(article_arq_ppa.span.a["href"])


def pdtic(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/governanca-de-tic/pdtic" 
    mi_page = page_access(url)
    title_pdtic = mi_page.find("h1", class_="documentFirstHeading").text
    post_pdtic = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_pdtic = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_pdtic = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_pdtic = []
    links_pdtic = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_pdtic in links_pdtic:
        list_links_pdtic.append(a_pdtic["href"])


def cgd(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/assuntos/planejamento-e-gestao/governanca-de-tic/comite-de-governanca-digital-cgd" 
    mi_page = page_access(url)
    title_cgd = mi_page.find("h1", class_="documentFirstHeading").text
    post_cgd = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cgd = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_cgd = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_cgd = []
    links_cgd = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cgd in links_cgd:
        list_links_cgd.append(a_cgd["href"])


def auditorias(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/auditorias" 
    mi_page = page_access(url)
    title_auditorias = mi_page.find("h1", class_="documentFirstHeading").text
    post_auditorias = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_auditorias = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_auditorias = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_auditorias = []
    links_auditorias = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_auditorias in links_auditorias:
        list_links_auditorias.append(a_auditorias["href"])


def dados(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/dados-abertos-1" 
    mi_page = page_access(url)
    title_dados = mi_page.find("h1", class_="documentFirstHeading").text
    post_dados = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_dados = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_dados = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_dados = []
    links_dados = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_dados in links_dados:
        list_links_dados.append(a_dados["href"])


def demonstracoes(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/demonstracoes-contabeis" 
    mi_page = page_access(url)
    title_demonstracoes = mi_page.find("h1", class_="documentFirstHeading").text
    post_demonstracoes = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_demonstracoes = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_demonstracoes = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_demonstracoes = []
    links_demonstracoes = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_demonstracoes in links_demonstracoes:
        list_links_demonstracoes.append(a_demonstracoes["href"])


def rel_gestao(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/relatorio-de-gestao" 
    mi_page = page_access(url)
    title_rel_gestao = mi_page.find("h1", class_="documentFirstHeading").text
    post_rel_gestao = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_rel_gestao = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_rel_gestao = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_rel_gestao = []
    links_rel_gestao = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_rel_gestao in links_rel_gestao:
        list_links_rel_gestao.append(a_rel_gestao["href"])


def responsaveis(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/rol-de-responsaveis" 
    mi_page = page_access(url)
    title_responsaveis = mi_page.find("h1", class_="documentFirstHeading").text
    post_responsaveis = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_responsaveis = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    content_responsaveis = mi_page.find("div", {"id":"parent-fieldname-text"}).text
    # links
    list_links_responsaveis = []
    links_responsaveis = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_responsaveis in links_responsaveis:
        list_links_responsaveis.append(a_responsaveis["href"])


def cronologia(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/cronologia-de-pagamentos" 
    mi_page = page_access(url)
    title_cronologia = mi_page.find("h1", class_="documentFirstHeading").text
    post_cronologia = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_cronologia = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_cronologia = []
    links_cronologia = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_cronologia in links_cronologia:
        list_links_cronologia.append(a_cronologia["href"])
    if list_links_cronologia[0]: # check
        cronologia_0 = page_access(list_links_cronologia[0])
        title_cronologia0 = cronologia_0.find("h1", class_="documentFirstHeading").text
        update_cronologia0 = cronologia_0.find("span", class_="documentModified").find("span", class_="value").text
        list_link_cronologia0 = []
        link_cronologia0 = cronologia_0.find("div", {"id":"content-core"}).find_all("a")
        for a_cronologia0 in link_cronologia0:
            list_link_cronologia0.append(a_cronologia0["href"]) 
    if list_links_cronologia[1]: # check
        cronologia_1 = page_access(list_links_cronologia[1])
        title_cronologia1 = cronologia_1.find("h1", class_="documentFirstHeading").text
        update_cronologia1 = cronologia_1.find("span", class_="documentModified").find("span", class_="value").text
        list_link_cronologia1 = []
        link_cronologia1 = cronologia_1.find("div", {"id":"content-core"}).find_all("a")
        for a_cronologia1 in link_cronologia1:
            list_link_cronologia1.append(a_cronologia1["href"])
    if list_links_cronologia[2]: # check
        cronologia_2 = page_access(list_links_cronologia[2])
        title_cronologia2 = cronologia_2.find("h1", class_="documentFirstHeading").text
        update_cronologia2 = cronologia_2.find("span", class_="documentModified").find("span", class_="value").text
        list_link_cronologia2 = []
        link_cronologia2 = cronologia_2.find("div", {"id":"content-core"}).find_all("a")
        for a_cronologia2 in link_cronologia2:
            list_link_cronologia2.append(a_cronologia2["href"])
    if list_links_cronologia[3]: # check
        cronologia_3 = page_access(list_links_cronologia[3])
        title_cronologia3 = cronologia_3.find("h1", class_="documentFirstHeading").text
        update_cronologia3 = cronologia_3.find("span", class_="documentModified").find("span", class_="value").text
        list_link_cronologia3 = []
        link_cronologia3 = cronologia_3.find("div", {"id":"content-core"}).find_all("a")
        for a_cronologia3 in link_cronologia3:
            list_link_cronologia3.append(a_cronologia3["href"])


def convenios(): # check
    url = "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/conteudo-convenios-e-transferencias" 
    mi_page = page_access(url)
    title_convenios = mi_page.find("h1", class_="documentFirstHeading").text
    post_convenios = mi_page.find("span", class_="documentPublished").find("span", class_="value").text
    update_convenios = mi_page.find("span", class_="documentModified").find("span", class_="value").text
    # links
    list_links_convenios = []
    links_convenios = mi_page.find("div", {"id":"content-core"}).find_all("a")
    for a_convenios in links_convenios:
        list_links_convenios.append(a_convenios["href"])
    if list_links_convenios[0]: # check
        convenios_0 = page_access(list_links_convenios[0])
        title_convenios0 = convenios_0.find("h1", class_="documentFirstHeading").text
        update_convenios0 = convenios_0.find("span", class_="documentModified").find("span", class_="value").text
        list_link_convenio0 = []
        link_convenio0 = convenios_0.find("div", {"id":"content-core"}).find_all("a")
        for a_convenio0 in link_convenio0:
            list_link_convenio0.append(a_convenio0["href"])
    if list_links_convenios[1]: # check
        convenios_1 = page_access(list_links_convenios[1])
        title_convenios1 = convenios_1.find("h1", class_="documentFirstHeading").text
        update_convenios1 = convenios_1.find("span", class_="documentModified").find("span", class_="value").text
        list_link_convenio1 = []
        link_convenio1 = convenios_1.find("div", {"id":"content-core"}).find_all("a")
        for a_convenio1 in link_convenio1:
            list_link_convenio1.append(a_convenio1["href"])
    if list_links_convenios[2]: # check
        convenios_2 = page_access(list_links_convenios[1])
        title_convenios2 = convenios_2.find("h1", class_="documentFirstHeading").text
        update_convenios2 = convenios_2.find("span", class_="documentModified").find("span", class_="value").text
        list_link_convenio2 = []
        link_convenio2 = convenios_2.find("div", {"id":"content-core"}).find_all("a")
        for a_convenio2 in link_convenio2:
            list_link_convenio2.append(a_convenio2["href"])
        

def main():
    global bs
    url = "https://www.gov.br/infraestrutura/pt-br"
    bs = page_access(url) 
    mi_noticias = noticias() 
    mi_arq_rel = arq_rel() 
    mi_ri = ri() 
    mi_planos = planos() 
    mi_rel_orc = rel_orc() 
    mi_ppa = ppa() 
    mi_arq_ppa = arq_ppa() 
    mi_pdtic = pdtic() 
    mi_cgd = cgd() 
    mi_auditorias = auditorias() 
    mi_dados = dados() 
    mi_demonstracoes = demonstracoes() 
    mi_rel_gestao = rel_gestao() 
    mi_responsaveis = responsaveis() 
    mi_cronologia = cronologia() 
    mi_convenios = convenios()


if __name__ == "__main__":
    main()