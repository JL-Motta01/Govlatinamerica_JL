from yattag import Doc, indent
from tinydb import TinyDB, Query, where
from dotenv import load_dotenv
import os
import sys
DIR_PWD = os.environ["PWD"] 
lista_dir_atual = DIR_PWD.split("/")
NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
lista_dir_atual_02 = DIR_PWD.split(NOME_PROJETO)
DIR_PROJETO = lista_dir_atual_02[0]+NOME_PROJETO
sys.path.append(DIR_PROJETO) 
if NOME_PROJETO == "templates":
    from diretorios.diretorio import diretorios, diretorios_template 
else:
    from templates.diretorios.diretorio import diretorios, diretorios_template 
print(f'DIR PROJETO: {DIR_PROJETO}')


def html_consultar_json(sites="NA", template="NA"):
    print("Acessando função geradora dos HTML")
    if str(sites):
        lista_sites = [sites]
        print(f'LISTA COM UM SITE: {lista_sites}')
    else: 
        lista_sites = sites
        print(f'LISTA COM MAIS DE UM SITE: {lista_sites}')
    for site in lista_sites:
        if template == "ok":
            print("ok")
            diretorio = diretorios_template(site)
        else:
            diretorio = diretorios(site)
        dir_json = diretorio[0]
        dir_html = diretorio[1]
        dir_referencias = diretorio[3]
        dir_estilo = diretorio[4]
        print(f'dir_estilo: {dir_estilo}')
        db = TinyDB(f'{dir_json}/json/{site}.json')
        myDBQuery = Query()
        for dado in iter(db):
            origem = dado['origem']
            sigla = dado['sigla']
            classificado = dado['classificado']
            titulo = dado['titulo']
            subtitulo = dado['subtitulo']
            link = dado['link']
            link_archive = dado['link_archive']
            data_archive = dado['data_archive']
            horario_archive = dado['horario_archive']
            categoria = dado['categoria']
            data = dado['data']
            horario = dado['horario']
            data_atualizado = dado['data_atualizado']
            horario_atualizado = dado['horario_atualizado']
            local = dado['local']
            autoria = dado['autoria']
            tags = dado['tags']
            paragrafos = dado['paragrafos']
            nome_arquivo = dado['nome_arquivo']
            imagens = dado['imagens']
            dir_bd = dado['dir_bd']
            codigo_bd = dado['codigo_bd']
            extra_01 = dado['extra_01']
            extra_02 = dado['extra_02']
            extra_03 = dado['extra_03']
            print(f'DATA: {data}')
            if template == "ok":
                dir_html_ano = diretorios_template(site, f'{data[-4:]}/{data[3:5]}/{data[:2]}')[2]
            else:
               dir_html_ano = diretorios(site, f'{data[-4:]}/{data[3:5]}/{data[:2]}')[2]
            html = gerar_html(dir_html_ano, dir_referencias, dir_estilo, dir_html, origem, sigla, classificado, titulo, subtitulo, link, link_archive, data_archive, horario_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, nome_arquivo, imagens, dir_bd, codigo_bd, extra_01, extra_02, extra_03)
            atualizar_banco = atualiza_json(html, site)

            print("#################")
            print("#################")

def gerar_html(dir_html_ano="NA", dir_referencias="NA", dir_estilo="NA", dir_html="NA", origem="NA", sigla="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", data_archive="NA", horario_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA", nome_arquivo="NA", imagens="NA", dir_bd="NA", codigo_bd="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
    doc, tag, text = Doc().tagtext()
    paragrafos_avisos = [f'Este texto deve ser utilizado somente para fins acadêmicos. Para qualquer outro fim entrar em contato com a instituição que produziu e/ou divulgou esta informação: {origem}']
    links = ["stylesheet"]
    ESTILO = dir_estilo
    REFERENCIAS = dir_referencias
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8" />')
            for l in links:
                #doc.asis(f'<link rel={l} type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">')
                #doc.asis(f'<link rel={l} type="/home/labri_juliasilveira/codigo/newscloud/template/reset.css">')
                doc.asis(f'<link rel={l} type="text/css" href={ESTILO}>')
                #doc.asis(f'<link rel={l} type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">')
            doc.asis(f'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
            doc.asis(f'<meta name="origem" content="{origem}">') 
            doc.asis(f'<meta name="sigla" content="{sigla}">')
            doc.asis(f'<meta name="classificado" content="{classificado}">') 
            doc.asis(f'<meta name="titulo" content={titulo}>') 
            doc.asis(f'<meta name="subtitulo" content={subtitulo}>')
            doc.asis(f'<meta name="link" content={link}>') 
            doc.asis(f'<meta name="link_archive" content={link_archive}>')
            doc.asis(f'<meta name="data_archive" content={data_archive}>')
            doc.asis(f'<meta name="horario_archive" content={horario_archive}>')
            doc.asis(f'<meta name="data" content="{data}">')
            doc.asis(f'<meta name="horario" content="{horario}">')
            doc.asis(f'<meta name="data_atualizado" content="{data_atualizado}">') 
            doc.asis(f'<meta name="horario_atualizado" content="{horario_atualizado}">') 
            doc.asis(f'<meta name="local" content={local}>') 
            doc.asis(f'<meta name="autoria" content={autoria}>') 
            doc.asis(f'<meta name="nome_arquivo" content={nome_arquivo}>') 
            doc.asis(f'<meta name="imagens" content={imagens}>') 
            doc.asis(f'<meta name="tags" content="{tags}">') 
            doc.asis(f'<meta name="dir_bd" content="{dir_bd}">') # meta tag >> dado sobre os dados / dados sobre a pag.
            doc.asis(f'<meta name="codigo_bd" content="{codigo_bd}">')

        with tag('body'):
            with tag('div', klass='container'):
                with tag('article', klass="texto-conteudo", id="conteudo-principal"):
                    with tag('div', klass='head-noticia'):
                        with tag('h1'):
                            text(titulo)
                        with tag('h2', klass='subtitulo'):
                            if subtitulo != 'NA':
                                text(subtitulo)
                                
                    with tag('div', klass='corpo-noticia'):
                        with tag('p', id='negrito'):
                            if "NA" in autoria:
                                text(f'{origem.title()}, {data}')
                            else: 
                                text(f'{", ".join(autoria)}, {data}')
                        for paragrafo in paragrafos:
                            with tag('p'):
                                text(paragrafo)

                if not 'NA' in imagens:
                    with tag('div', klass='container'):
                        with tag('h2'):
                            text(f'Imagens')
                        with tag('figure'):
                            for imagem in imagens:
                                doc.stag('img', src=imagem, klass='imagem')


                with tag('div', klass='referencia', id='referencias'):
                    with tag('h2'):
                        #text(f'Como citar: {origem}. {titulo}, {data}. Acesso em: ')
                        #doc.asis(f'<span id="dateAndTime">Como citar: {origem}. {titulo}, {data}. Acesso em: </span>')
                        # MINISTERIODACIDADANIA. 12ª Conferência Nacional da Assistência Social tem Início em Brasília, 16/12/2021, Acesso em: 11 jan. 2022
                        text(f'Como citar ')
                    with tag('h4'):
                        text(f'{origem.upper()}. ')
                        with tag('span', id='negrito'):
                            text(f'{titulo}, ')
                        text(f'{data}. ')
                        text(f'Disponível em: {link}. ')
                        text(f'Acesso em: ')
                        with tag('span', id='dateAndTime'):
                            text(f'Acesso em: ')


                with tag('header', klass="negrito", id="metadados"):
                    with tag('h2'):
                        text('Metadados')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in autoria:
                                text(f'Origem: {origem.title()}')
                            else: 
                                text(f'Autoria: {", ".join(autoria)}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if classificado == "NA":
                                text(f'Classificado como: Informação Ausente')
                            else: 
                                text(f'Classificado como: {classificado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if data == "NA":
                                text(f'Data: Informação Ausente')
                            text(f'Data: {data}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if horario == "NA":
                                text(f'Horario: Informação Ausente')
                            text(f'Horario: {horario}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if data_atualizado == "NA":
                                text(f'Data de atualização: Informação Ausente')
                            else:
                                text(f'Data de atualização: {data_atualizado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if horario_atualizado == "NA":
                                text(f'Horario de atualização: Informação Ausente')
                            else:
                                text(f'Horario de atualização: {horario_atualizado}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if local == "NA":
                                text(f'Local: Informação Ausente')
                            else: 
                                text(f'Local: {local}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if nome_arquivo == "NA":
                                text(f'Nome do arquivo: Informação Ausente')
                            else: 
                                text(f'Nome do arquivo: {nome_arquivo}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in tags:
                                text(f'Tags: Informação Ausente')
                            else: 
                                text(f'Tags: {", ".join(tags)}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in link:
                                text(f'Endereço original: Informação Ausente')
                            else: 
                                text(f'Endereço original: ')
                                with tag('a', href=link, target="_blank"):
                                    text("Acesse aqui o link original desta informação")
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in link_archive:
                                text(f'Endereço no Internet Archive: Informação Ausente')
                            else:  
                                text(f'Endereço no Internet Archive: ')
                                with tag('a', href=link, target="_blank"):
                                    text("Acesse aqui o link arquivado no Internet Archive")
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in data_archive:
                                text(f'Arquivado no Internet Archive em: Informação Ausente')
                            else:  
                                text(f'Arquivado no Internet Archive em: {data_archive}')
                    with tag('h3'):
                        with tag('span', klass="infos"):
                            if "NA" in horario_archive:
                                text(f'Arquivado no Internet Archive às: Informação Ausente')
                            else:  
                                text(f'Arquivado no Internet Archive às: {horario_archive[0]} ({horario_archive[1]})')
                    with tag('h3'):
                        with tag('span', klss="infos"):
                            if "NA" in codigo_bd:
                                text(f'Código Base de Dados: Informação ausente')
                            else: 
                                text(f'Código Base de Dados: {codigo_bd}')

                



            with tag('footer', klass="aviso"):
                with tag('div', klass='aviso-texto'):
                    text("AVISOS")
                    for paragrafo in paragrafos_avisos:
                        with tag('h5'):
                            text(paragrafo)
            doc.asis(f'<script type="text/javascript" src={REFERENCIAS}></script>')
    # result = indent(doc.getvalue())
    result = doc.getvalue()
    print(f'DIR HTML ANO: {dir_html_ano}')

    if "/" or ":" in titulo:
        titulo_html = titulo.replace("/", "-").replace(":", "_").replace(" ", "_")
    else: 
        titulo_html = titulo
    if ":" in horario:
        horario_html = horario.replace(":", "_")
    else: 
        horario_html = horario

    dir_arquivo = dir_html_ano
    nome_arquivo = f'{data[-4:]}-{data[3:5]}-{data[:2]}-{horario_html}-{sigla}-{titulo_html}.html'
    with open(f"{dir_html_ano}/{nome_arquivo}", "w") as file:
        file.write(result)
    return dir_arquivo, nome_arquivo, link

def atualiza_json(html, nome, template="NA"):
    dir_arquivo = html[0] 
    nome_arquivo = html[1]
    url = html[2]
    if template == "ok":
        dir_banco = diretorios_template(nome)[0]
    else:
        dir_banco = diretorios(nome)[0]
    db = TinyDB(f'{dir_banco}/json/{nome}.json', ensure_ascii=False)
    db.update_multiple([
        ({"dir_arquivo": dir_arquivo}, where("link")==url),
        ({"nome_arquivo": nome_arquivo}, where("link")==url),
        ])

def main():
    sites = ["CIDADANIA2", "MEC"]
    consulta = html_consultar_json(sites, template="ok")

if __name__ == '__main__':
    main()

    