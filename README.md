# Coleta de Dados de sites governamentais da América Latina

## Informações Importantes

| Conteúdo           | Link de Acesso                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| Código das Coletas | [Repositório GitLab](https://gitlab.com/unesp-labri/projeto/govlatinamerica)                       |
| Informações gerais | [Pasta Google Drive](https://drive.google.com/drive/u/1/folders/1_g01RcccLl2PpTupxQyCoXEJka30VXeG) |
| Tarefas do projeto | [Notion](https://www.notion.so/Projeto-GovLatinAmerica-9219a9b60ae24cb98a197f7bdab42209)           |
| Documentação       | [Site](https://apoio.labriunesp.org/docs/projetos/dados/gov-latin-america/intro/)                  |
| Template html      | [Template html](https://gitlab.com/unesp-labri/projeto/template-html)                              |


# Sincronizar com o GitLab (na pasta raiz GOVLATINAMERICA)

git pull origin main && conda activate env_govlatinamerica2 && conda env update --prune

```
git add .
git commit -m "comentário"
git pull origin main
git push origin main
```

 # Pendências
- [x] definir variáveis de ambiente 
- [x] resolver questões de importação
- [x] deixar mais genérico o template html
- [x] ajustar caminhos para estilos e referências do html
- [x] separar em um template a inserção no banco de dados 
- [x] separar em um template os apontamentos dos diretórios 
- [x] separar em um template o internet archive 
- [x] salvar os arquivos no internet archive 
- [ ] cada projeto/repositório deve ter o seu próprio .env_dir
- [ ] ajustar link e link_archive para url e url_archive
- [x] inserir no json a data em que o link foi salvo no internet archive
- [ ] fazer uma chamada genérica no internet archive (em andamento)
- [ ] documentar estrutura dos repositórios do gitlab
- [x] acrescentar na função inserir_bd os parâmetros data_archive e horario_archive: ambos inicialmente como N/A
- [x] integrar template ao projeto GovLatinAmerica (em andamento)
- [ ] ver questões de importação (repositório template govlatinamerica)
  - [ ] otimizar importação 
  - [ ] criar script main.py na raiz
  - [ ] utilizar setup.py
- [x] ver caminho do css no govlatinamerica
- [x] apontar sites para coleta
- [ ] verificar diretórios em que os arquivos HTML's e Jsons são salvos
- [ ] TRATAMENTO DAS NOTAS DE IMPRENSA DE 1997 A 2013
  - [ ] verificar problema de encode de 2013
  - [x] verificar todas as informações importantes contidas no html (título, data, parágrafos, número da nota quando houver...)
  - [ ] corrigir problema na autoria
  - [ ] verificar se variáveis do json estão em conformidade com os templates
  - [ ] substituir as quebras de linha (\n) por espaço em cada parágrafo
  - [x] necessidade de tratar especificamente as datas e os parágrafos de cada ano (mudança de estrutura html)
  - [ ] inserir no banco de dados (em andamento)
  - [ ] gerar htmls (em andamento)
  - [ ] arquivar no internet archive nossos htmls locais
  
- [ ] SITE PLANALTO
  -[ ] substituir downloads wget por requests
  



  # Integração 

- Notícias
- Agenda
- HTML

|Ministério|Notícias|Agenda|
|----------|--------|------|
|[Planalto](https://www.gov.br/planalto/pt-br) | Específico |  Comum    |
|[Casa Civil](https://www.gov.br/casacivil/pt-br)| Comum | Comum |
|[MRE](https://www.gov.br/mre/pt-br/)| Específico | Comum |
|[MMA](https://www.gov.br/mma/pt-br)| Específico | Comum |
|[Infraestrutura](https://www.gov.br)|Específico | Comum |
|[MME](https://www.gov.br/mme/pt-br)| Comum | Comum |
|[Economia](https://www.gov.br/economia/pt-br)| Comum | Sem agenda (fora do ar temporariamente) |
|[Defesa](https://www.gov.br/defesa/pt-br)| Comum | Comum |
|[Saúde](https://www.gov.br/saude/pt-br)| Comum | Comum |
|[Ciência](https://www.gov.br/mcti/pt-br)| Comum | Comum |
|[Mulher](https://www.gov.br/mdh/pt-br/)| Específico | Comum |
|[Comunicações](https://www.gov.br/mcom/pt-br/)| Comum | Comum |
|[Turismo](https://www.gov.br/turismo/pt-br)| Comum | Apenas agenda antiga / Agenda desconfiguada|
|[Desenvolvimento Regional](https://www.gov.br/mdr/pt-br)| Comum | Apenas agenda antiga|
|[Biblioteca presidencia](https://www.gov.br/planalto/pt-br/conheca-a-presidencia/acervo/biblioteca-da-presidencia)| Sem notícias | Sem agenda |
|[Secretaria-Geral](https://www.gov.br/secretariageral/pt-br)| Específico | Comum |
|[Controladoria-Geral da União](https://www.gov.br/cgu/pt-br)| Específico | Comum |
|[Advocacia-Geral da União](https://www.gov.br/agu/pt-br)| Específico | Comum |
|[Cidadania (institucional)](https://www.gov.br/cidadania/pt-br)| Comum (>> dá problema a partir da 9ª notícia) | Específico |  
|[Cidadania (desenvolvimento social)](https://www.gov.br/cidadania/pt-br)| Específico | Específico |
|[Cidadania (esporte)](https://www.gov.br/cidadania/pt-br)| Específico | Específico |
|[Secretaria de Governo](https://www.gov.br/secretariadegoverno/pt-br)| Comum | Comum|
|[Educação](https://www.gov.br/mec/pt-br)| Comum | Agenda antiga apenas |
|[Ministério da Justiça e Segurança Pública](https://www.gov.br/mj/pt-br)| Comum | link específico |
|[Gabinete de Segurança Institucional](https://www.gov.br/gsi/pt-br)| Específico | link específico|
|[MAPA](https://www.gov.br/agricultura/pt-br/)| Comum | link específico|

# Problemas no GIT

## non-fast-forward

```
git add --all .
git commit -m "resolvendo conflitos no arquivo html template e teste de internet archive"
git pull origin main
git push origin main
git subtree pull --prefix=templates templates main
git subtree push --prefix=templates templates main

``` 

# Para adicionar repositórios externos

```
git remote add templates https://gitlab.com/unesp-labri/projeto/templates.git
git subtree add --prefix=templates/ templates main

```