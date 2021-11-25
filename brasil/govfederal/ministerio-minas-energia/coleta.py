from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  # retorna a página da função links_navigation
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def noticias():
    url = "https://www.gov.br/mme/pt-br/assuntos/noticias" 
    mme_page = page_access(url)


def pdp21():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/institucional/acoes-de-desenvolvimento-de-pessoas/plano-de-desenvolvimento-de-pessoas-2013-pdp-mme-2021" 
    mme_page = page_access(url)


def pdp20():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/institucional/acoes-de-desenvolvimento-de-pessoas/plano-de-desenvolvimento-de-pessoas-2013-pdp-mme-2020" 
    mme_page = page_access(url)


def contasanuais():
    url = "https://www.gov.br/mme/pt-br/acesso-a-informacao/auditorias/processos-de-contas-anuais" 
    mme_page = page_access(url)


def contratacoes():
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
    url = "https://www.gov.br/infraestrutura/pt-br"
    bs = page_access(url) 
    mme_noticias = noticias()
    mme_pdp21 = pdp21()
    mme_pdp20 = pdp20()
    mme_contasanuais = contasanuais()
    mme_contratacoes = contratacoes()
    mme_contratos = contratos()
    mme_luz_amaz = luz_amaz()
    mme_metas_inst = metas_inst()
    mme_discursos = discursos()
    mme_apresentacoes = apresentacoes()
    mme_boletins_covid = boletins_covid()
    mme_informativo = informativo()
    mme_boletins_mensais = boletins_mensais()
    mme_resenha = resenha()
    mme_doc_potee = doc_potee()
    mme_doc_30 = doc_30()
    mme_relatorios = relatorios()


if __name__ == "__main__":
    main()