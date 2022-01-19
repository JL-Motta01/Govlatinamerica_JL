import waybackpy
from waybackpy import WaybackMachineSaveAPI

def salvar_pagina():
    url = "https://www.gov.br/mj/pt-br/assuntos/noticias/ministerio-da-justica-e-seguranca-publica-realiza-segunda-etapa-dos-ensaios-tecnicos-em-viaturas"
    user_agente = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
    wayback = waybackpy.Url(url, user_agente)
    archive = wayback.save()
    print(archive.archive_url)

def salvar_pagina2():
    url = "https://github.com"
    user_agente = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    save_api = WaybackMachineSaveAPI(url, user_agente)
    arquivar_pagina = save_api.save()
    arquivar_data = save_api.timestamp()
    print(arquivar_pagina)
    print(arquivar_data)

def main():
    salvar = salvar_pagina2()

if __name__=="__main__":
    main()