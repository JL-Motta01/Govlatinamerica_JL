from coleta_noticias import NoticiasGovBr
from yattag import Doc, indent
from tinydb import TinyDB, Query

def consultar():
    govbr = NoticiasGovBr()
    diretorios = govbr.diretorio("CIDADANIA")
    dir_json = diretorios[0]
    dir_html = diretorios[1]
    db = TinyDB(f'{dir_json}/CIDADANIA.json')
    myDBQuery = Query()
    for dado in iter(db):
        origem = dado['origem']
        classificado = dado['classificado']
        titulo = dado['titulo']
        subtitulo = dado['subtitulo']
        link = dado['link']
        link_archive = dado['link_archive']
        categoria = dado['categoria']
        data = dado['data']
        horario = dado['horario']
        data_atualizado = dado['data_atualizado']
        horario_atualizado = dado['horario_atualizado']
        local = dado['local']
        autoria = dado['autoria']
        tags = dado['tags']
        paragrafos = dado['paragrafos']
        dir_local = dado['dir_local']
        extra_01 = dado['extra_01']
        extra_02 = dado['extra_02']
        extra_03 = dado['extra_03']
        print(data)
        template_html(dir_html, origem, classificado, titulo, subtitulo, link, link_archive, categoria, data, horario, data_atualizado, horario_atualizado, local, autoria, tags, paragrafos, dir_local, extra_01, extra_02, extra_03)
        
        print("#################")
        print("#################")

def template_html(dir_html="NA", origem="NA", classificado="NA", titulo="NA", subtitulo="NA", link="NA", link_archive="NA", categoria="NA", data="NA", horario="NA", data_atualizado="NA", horario_atualizado="NA", local="NA", autoria="NA", tags="NA", paragrafos="NA", dir_local="NA", extra_01="NA", extra_02="NA", extra_03="NA"):
    doc, tag, text = Doc().tagtext()
    links = ["stylesheet"]
    infos=['subtitulo', 'autoria']
    paragrafos = "NA"
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8" />')
            for l in links:
                doc.asis(f'<link rel={l} type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">')
                doc.asis(f'<link rel={l} type="template/reset.css">')
                doc.asis(f'<link rel={l} type="text/css" href="template/style.css">')
                doc.asis(f'<link rel={l} type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">')
            doc.asis(f'<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
            doc.asis(f'<meta name="origem" content="{origem}">') 
            doc.asis(f'<meta name="classificado" content="{classificado}">') 
            doc.asis(f'<meta name="titulo" content={titulo}>') 
            doc.asis(f'<meta name="subtitulo" content={subtitulo}>') 
            doc.asis(f'<meta name="link" content={link}>') 
            doc.asis(f'<meta name="link_archive" content={link_archive}>')
            doc.asis(f'<meta name="categoria" content={categoria}>')  
            doc.asis(f'<meta name="data" content="{data}">') 
            doc.asis(f'<meta name="horario" content={horario}>') 
            doc.asis(f'<meta name="data_atualizado" content={data_atualizado}>') 
            doc.asis(f'<meta name="horario_atualizado" content={horario_atualizado}>') 
            doc.asis(f'<meta name="local" content="{local}">')  
            doc.asis(f'<meta name="autoria" content="{autoria}">')
            doc.asis(f'<meta name="tags" content="{tags}">')  
            doc.asis(f'<meta name="dir_local" content="{dir_local}">')
            doc.asis(f'<meta name="extra_01" content="{extra_01}">')
            doc.asis(f'<meta name="extra_02" content="{extra_02}">')
            doc.asis(f'<meta name="extra_03" content="{extra_03}">')
        with tag('body'):
            with tag('div', klass='container'):
                with tag('header', klass="negrito", id="conteudo-principal"):
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Origem: {origem.title()}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Classificado como : {classificado}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Data: {data}')
                    with tag('h2'):
                        with tag('span', klass="info-head"):
                            text(f'Atualizado em: {data_atualizado}')
        
                with tag('article', klass="texto-conteudo", id="conteudo-principal"):
                    with tag('div', klass='head-noticia'):
                        with tag('h1'):
                            text(titulo)
                        with tag('p'):
                             text(subtitulo)
                        with tag('p'):
                             text(autoria)
                                
                    with tag('div', klass='corpo-noticia'):
                        for paragrafo in paragrafos:
                            with tag('p'):
                                text(paragrafo)
                with tag('div', klass='referencia'):
                    with tag('h2'):
                        text("Como citar")



            with tag('footer', klass="aviso"):
                with tag('div', klass='aviso-texto'):
                    text("AVISOS")
                with tag('field1', name='blah'):
                    text('some value1')


    """
    result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
    )
    """
    result = doc.getvalue()


    with open(f"{dir_html}/{titulo}.html", "w") as file:
        file.write(result)
    


def main():
    consulta = consultar()


if __name__ == '__main__':
    main()