import savepagenow 

def salvar_pagina():
    arquivar = savepagenow.capture("https://www.gov.br/mj/pt-br/assuntos/noticias/ministerio-da-justica-e-seguranca-publica-realiza-segunda-etapa-dos-ensaios-tecnicos-em-viaturas")

def main():
    salvar = salvar_pagina()

if __name__=="__main__":
    main()