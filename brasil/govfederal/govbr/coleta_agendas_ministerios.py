import urllib.request #realizar requisição da página html
from tinydb import TinyDB,Query
from bs4 import BeautifulSoup #importa o beautifulsoup para extrair as infos das tags
from pprint import pprint #organizar estéticamente os prints
from datetime import date, timedelta, datetime
import os
import sys 
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO)
from templates.diretorios.diretorio import diretorios
from templates.acesso_bd.inserir_bd import inserir_bd

# DIR_LOCAL= "/home/labri_joaomotta/codigo"
# DIR_DADOS= "/media/hdvm10/bd/003/001/001/001/001-b"


def acessar_pagina(url):
    """Analisa os boletim do site a partir do link"""
    global response
    global html
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response, 'lxml', from_encoding = response.info().get_param("charset"))
    return html

def datas():
    data_inicio = date (2019,1,1)
    data_fim = date.today()
    delta = data_fim - data_inicio
    lista_data = []
    for dia in range(delta.days+1):
        dia_delta = data_inicio + timedelta(days=dia)
        lista_data.append(dia_delta)
    lista_data_final = [datetime.strftime(dt,format="%Y-%m-%d") for dt in lista_data]
    return lista_data_final

def agenda(urlbase):
    """Percorre as datas da agenda"""
    #lista_data = datas()
    lista_data = ["2021-11-10","2021-11-11"]
    url_base = urlbase
    lista_url_data = []
    for data in lista_data:
        url= url_base+("/")+data
        lista_url_data.append(url)
    print("---- LISTA URL COM DATA ----")
    print(lista_url_data)
    return lista_url_data

def coleta_compromissos(ag,origem):
    """coleta os compromissos de cada dia"""
    for dia in agenda(ag):
        dir_json = diretorios("PLANALTO")[0]
        db = TinyDB(f"{dir_json}/agenda_ministerios.json", indent=4, ensure_ascii=False)
        User = Query()
        try:
            pagina_dia = acessar_pagina(dia)
            url=dia
            data=pagina_dia.find("span", {"id":"breadcrumbs-current"}).text
            print(f"DATA:{data}")
            print("---- DIA ENCONTRADO NA AGENDA ----")
            try:
                try:
                    lista_conteudo=[]
                    compromissos = pagina_dia.find("ul", class_="list-compromissos").find_all("div", class_="item-compromisso")
                    for conteudo in compromissos:
                        detalhes=[]
                        titulo=conteudo.find("h2", class_="compromisso-titulo").text
                        print(titulo)
                        detalhes.append(titulo)
                        horario=conteudo.find("div", class_="horario").text
                        detalhes.append(horario)
                        local=conteudo.find("div", class_="compromisso-local").text
                        detalhes.append(local)
                        detalhes.append(data)
                        detalhes.append(url)
                        lista_conteudo.append(detalhes)
                except:
                    lista_conteudo= "NA" 
                for detalhe in lista_conteudo:
                    print(detalhe)
                    db_planalto = db.contains((User.link==detalhe[4])&(User.titulo==detalhe[0])&(User.data==detalhe[3][-10:])&(User.horario==detalhe[1].replace("              ","").replace("\n","")))
                    if not db_planalto:
                        print("não está na base")
                        db.insert({
                            "origem" : origem,
                            "classificado_como" : "compromiso de agenda",
                            "titulo" : detalhe[0],
                            "subtitulo" : "NA",
                            "link" : detalhe[4],
                            "link_archive" : "NA",
                            "data" : detalhe[3][-10:],
                            "horario" : detalhe[1].replace("              ","").replace("\n",""), 
                            "data_atualizado_em" : "NA", 
                            "horario_atualizado_em" : "NA",
                            "local_do_compromisso" : detalhe[2],
                            "autoria" : detalhe[3][:10],
                            "tags" : "NA",
                            "conteudo" : "NA",
                            "dir_local" : "/media/hdvm10/bd/003/001/001/001/001-b/govlatinamerica/brasil/govfederal/govbr/bd"
                            })
                    else:
                        print("está na base")
            except:
                print("erro na inserção")
        except:
            print("Dia vazio na agenda")
            
def acesso_ministerios ():
    lista_ministerios = [
        "https://www.gov.br/casacivil/pt-br/acesso-a-informacao/agendas-da-casa-civil",
        "https://www.gov.br/mre/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/mma/pt-br/acesso-a-informacao/agenda-de-autoridades-1",
        "https://www.gov.br/infraestrutura/pt-br/acesso-a-informacao/agendas-de-autoridades",
        "https://www.gov.br/mme/pt-br/acesso-a-informacao/agendas-de-autoridades",
        "https://www.gov.br/defesa/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/economia/pt-br/acesso-a-informacao/agendas-de-autoridades",
        "https://www.gov.br/saude/pt-br/acesso-a-informacao/agenda-de-autoridades/",
        "https://www.gov.br/mcti/pt-br/acesso-a-informacao/agenda-de-autoridades/",
        "https://www.gov.br/mdh/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/mcom/pt-br/agenda-de-autoridades/",
        "https://www.gov.br/secretariageral/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/cgu/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/agu/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/secretariadegoverno/pt-br",
        "https://www.gov.br/gsi/pt-br/acesso-a-informacao/institucional/agendas-do-gsi",
        "https://www.gov.br/mj/pt-br/acesso-a-informacao/agenda-de-autoridades",
        "https://www.gov.br/agricultura/pt-br/acesso-a-informacao/agendas"

        ]
    lista_agenda = []
    for ministerio in lista_ministerios:
        acesso_ministerio = acessar_pagina(ministerio)
        """Teste para ministerios difereines"""

        # if ministerio==lista_ministerios[0]:
        #     """Casa Civil"""
        #     print("Começando coleta: Agendas da Casa Civil")
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)
        
        # if ministerio==lista_ministerios[1]:
        #     """MRE"""
        #     print("Começando coleta: Agendas do MRE")
        #     lista_link=card_content(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[2]:
        #     """MMA"""
        #     print("Começando coleta: Agendas do MMA")
        #     ag=card_content_secretaria(acesso_ministerio)
        #     lista_link=correcao_agenda(ag)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[3]:
        #     """Infraestrutura"""
        #     "Começando coleta: Agendas do ministério da Infraestrutura"
        #     lista_link=normal_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[4]:
        #     """MME"""
        #     "Começando coleta: Agendas do MME"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[5]:
        #     """Ministério da defesa"""
        #     "Começando coleta: Agendas do Ministério da defesa"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[6]:
        #     """Ministério da economia"""
        #     "Começando coleta: Agendas do Ministério da Economia"
        #     #Caso não se enquadre, solicita revisão do ministério (Ministério da economia, atualmente fora do ar)
        #     print("rever ministério: ", ministerio)

        # if ministerio==lista_ministerios[7]:
        #     """Ministério da saúde"""
        #     "Começando coleta: Agendas do Ministério da saúde"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[8]:
        #     """Mcti"""
        #     "Começando coleta: Agendas do Ministério da ciência e tecnologia"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[9]:
        #     """MDH"""
        #     "Começando coleta: Agendas do ministério da Mulher, da Família e dos Direitos Humanos"
        #     lista_link=normal_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[10]:
        #     """Ministério das comunicações"""
        #     "Começando coleta: Agendas do Ministério ddas comunicações"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[11]:
        #     """secretaria-geral da união"""
        #     "Começando coleta: Agendas da secretaria-geral da união"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[12]:
        #     """controladoria-geral da união"""
        #     "Começando coleta: Agendas da controladoria-geral da união"
        #     lista_link=lista_link_simples(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[13]:
        #     """advocacia geral da união"""
        #     "Começando coleta: Agendas da advocacia geral da união"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)

        # if ministerio==lista_ministerios[14]:
        #     """secretaria de governo"""
        #     "Começando coleta: Agendas da secretaria de governo"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)
            
        # if ministerio==lista_ministerios[15]:
        #     """GSI"""
        #     "Começando coleta: Agendas do GSI"
        #     lista_link=drop_list(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)
        
        # if ministerio==lista_ministerios[16]:
        #     """Ministério da justiça"""
        #     "Começando coleta: Agendas do Ministério da justiça"
        #     lista_link=coleta_mj(acesso_ministerio)
        #     coleta_agendas(lista_link,ministerio)
        
        if ministerio==lista_ministerios[17]:
            """Ministério da Agricultura"""
            "Começando coleta: Agendas do Ministério da Agricultura"
            lista_link=coleta_mapa(acesso_ministerio)
            coleta_agendas(lista_link,ministerio)       

def card_content(acesso):
    #ministérios que direcionam para as agendas a partir de card contents (MRE)
    agendas = acesso.find_all("a", class_="govbr-card-content")
    lista_agenda = []
    for agenda in agendas:
        lista_agenda.append(agenda["href"])
    return lista_agenda

def card_content_secretaria(acesso):
    #ministérios que direcionam para as secretarias a partir de card contents (MMA)
    #Nesse caso, acessa cada secretaria e lista as agendas de seus membros, também em card contents
    lista_secretarias=[]
    agendas_simples=[]
    cards = acesso.find_all("a", class_="govbr-card-content")
    agenda_ministro = cards[0]
    skip_card = [cards[0],cards[8]]
    agendas_simples.append(agenda_ministro["href"])
    for item in cards:
        if item in skip_card:
            continue
        else:
            lista_secretarias.append(item["href"])
    for secretaria in lista_secretarias:
        cards_secretaria = acessar_pagina(secretaria)
        membros = cards_secretaria.find_all("a", class_="govbr-card-content")
        for membro in membros:
            agendas_simples.append(membro["href"])
    return agendas_simples

def drop_list(acesso):
    #Ministérios com uso de drop-down-lists que contém os links para as agendas (Casa civil, MME e Ministério da defesa)
    agendas = acesso.find_all("a", class_="calendario")
    lista_agenda = []
    for agenda in agendas:
        lista_agenda.append(agenda["href"])
    return lista_agenda

def normal_list(acesso):
    #Ministérios que usam listas simples de links para as agendas (Ministério da infraestrutura)
    agendas = acesso.find_all("a", class_="internal-link")
    lista_agenda = []
    for agenda in agendas:
        lista_agenda.append(agenda["href"])
    return lista_agenda

def lista_link_simples(acesso):
    #Ministérios que usam listas simples de links para as agendas (Ministério da infraestrutura)
    agendas = acesso.find_all("a", class_="internal-link")
    lista_agenda = []
    for agenda in agendas[:-1]:
        lista_agenda.append(agenda["href"])
    return lista_agenda

def correcao_agenda(agendas):
    #Verifica se o link  da agenda direciona para uma versão simplificada da mesma (Comum no MMA)
    #Neste caso, busca o link da agenda completa
    corrige_agenda = []
    for link in agendas:
        try:
            acesso_reduzido = acessar_pagina(link)
            div_link = acesso_reduzido.find("div", class_="agenda-tile-footer")
            link_completo = div_link.find_all("a")
            for item in link_completo:
                agenda_completa = item["href"]
                print(agenda_completa)
            corrige_agenda.append(agenda_completa)
        except:
            pass
    return corrige_agenda

def coleta_agendas (lista,ministerio):
    for link in lista:
        pagina_inicial = acessar_pagina(ministerio)
        origem = pagina_inicial.find("div", class_="site-name").find("a").text
        print("Coletando de:"+origem)
        coleta_compromissos(link,origem)

def coleta_mj (acesso):
    #Nesse caso, acessa cada secretaria e lista as agendas de seus membros, também em card contents
    lista_secretarias=[]
    agendas_simples=[]
    ext_link=[]
    l_geral = acesso.find_all("p", class_="callout")
    for item in l_geral:
         link = item.find("a")
         ext_link.append(link["href"])
    print(len(ext_link))
    agenda_ministro = ext_link[0]
    skip_link = [ext_link[0],ext_link[15],ext_link[16],ext_link[17],ext_link[18],ext_link[19],ext_link[20]]
    agendas_simples.append(agenda_ministro)
    for item in ext_link:
        if item in skip_link:
            continue
        else:
            lista_secretarias.append(item)
    for secretaria in lista_secretarias:
        cards_secretaria = acessar_pagina(secretaria)
        membros = cards_secretaria.find_all("a", class_="govbr-card-content")
        for membro in membros:
            agendas_simples.append(membro["href"])
    return agendas_simples

def coleta_mapa (acesso):
    #Nesse caso, acessa cada secretaria e lista as agendas de seus membros, também em card contents
    lista_secretarias=[]
    agendas_simples=[]
    cards = acesso.find_all("a", class_="govbr-card-content")
    agenda_ministro = cards[0]
    skip_card = [cards[0],cards[15]]
    agendas_simples.append(agenda_ministro["href"])
    for item in cards:
        if item in skip_card:
            continue
        else:
            lista_secretarias.append(item["href"])
    for secretaria in lista_secretarias:
        agendas = acessar_pagina(secretaria)
        links = agendas.find("div", class_="list-item").find_all("a")
        for item in links:
            agendas_simples.append(item["href"])
    return list(set(agendas_simples))

def main ():
    """Função principal"""
    acesso_ministerios()

if __name__ == "__main__":
    main()