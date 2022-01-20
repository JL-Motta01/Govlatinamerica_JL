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


def estudos_mercado_tecnologia():
    url = "https://www.gov.br/mre/pt-br/assuntos/ciencia-tecnologia-e-inovacao/estudos-de-mercado-e-de-tecnologias"
    mre_page = page_access(url)


def alertas_consular():
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/alertas/alertas"
    mre_page = page_access(url)


def noticias_consular():
    url = "https://www.gov.br/mre/pt-br/assuntos/portal-consular/alertas%20e%20noticias/noticias/colecao-de-noticias"
    mre_page = page_access(url)


def infos_classificadas():
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/informacoes-classificadas"
    mre_page = page_access(url)
    

def infos_classificadas():
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/dados-abertos"
    mre_page = page_access(url)
    

def cgrc():
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/gestao-e-governanca/governanca/comite-de-governanca-riscos-e-controle-cgrc"
    mre_page = page_access(url)


def pei_mre():
    url = "https://www.gov.br/mre/pt-br/acesso-a-informacao/gestao-e-governanca/governanca/planejamento-estrategico-institucional-do-mre-pei-mre"
    mre_page = page_access(url)


def entrevistas():
    url = "https://www.gov.br/mre/pt-br/centrais-de-conteudo/publicacoes/discursos-artigos-e-entrevistas"
    mre_page = page_access(url)


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
    mre_noticias = noticias()
    mre_estudos_mercado_tecnologia = estudos_mercado_tecnologia()
    mre_alertas = alertas()
    mre_noticias_consular = noticias_consular()
    mre_infos_classificadas = infos_classificadas()
    mre_cgrc = cgrc()
    mre_pei_mre = pei_mre()
    mre_entrevistas = entrevistas()
    mre_resenhas_peb = resenhas_peb()
    mre_ocde_boletins = ocde_boletins()



if __name__ == "__main__":
    main()