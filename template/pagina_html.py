def get_html(dado):
    return f"""
<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/reset.css">
        <link rel="stylesheet" type="template/reset.css">
        <link rel="stylesheet" type="text/css" href="template/style.css">
        <link rel="stylesheet" type="text/css" href="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/style.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    </head>
    <body>
        <div class="container">
    

            <article class="texto-conteudo" id="conteudo-principal" id="relativo">
                <div class="head-noticia">
                    <h1>{dado['titulo']}</h1>
                </div>
                <div class="corpo-noticia">
                    <p class="texto-noticia">{dado['conteudo']}</p>
                </div>
            </article>

        <footer class="info-projeto">
            <div class="texto-footer">
                <h6>Avisos</h6>
                <p>Este texto deve ser utilizado somente para fins acadêmicos. Para qualquer outro fim entrar em contato com o órgão governamenbtal responsável.</p>
                <p>O tratamento e disponibilização é realizada com o intuito de facilitar a pesquisa.</p>
                <p>Não é permitida qualquer atividade com fins lucrativos usando esse texto.</p>
                <p>O LabRI-UNESP não detem os direitos sobre texto.</p>
            </div>
        </footer>
        <script type="text/javascript" src="https://gl.githack.com/unesp-labri/sites/host-css-js/-/raw/master/fsp-css/referencias.js"></script>
      </body>
    </html>"""
