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

```
git add .
git commit -m "comentário"
git pull origin main
git push origin main
```

# Verificar atualizações do ambiente virtual

```
git pull origin main && conda activate env_govlatinamerica2 && conda env update --prune
```

# Pendências

- [x] documentar criação do ambiente virtual 
- [x] habilitar ambiente virtual na estação remota 
- [x] instalação do vscode 
- [x] indicar onde colocar os dados coletados 
- [x] separação da coleta dos ministérios restantes (em andamento)
- [ ] construir classes para abrigar as partes similares dos sites (em andamento)
- [x] salvar informações em um banco json (em andamento)
- [x] separar data de horário
- [x] colocar mais de um parâmetro de verificação antes de inserir no json (ex: título, data e horário)
- [x] indicar categorias do Ministério da Cidadania (esporte, institucional e desenvolvimento social)
- [ ] gerar HTMLs a partir do BD json (template construído, falta escalar)
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
- [ ] tratamento das notas de imprensa de 1997 a 2013
  - [ ] verificar problema de encode de 2013
  - [x] verificar todas as informações importantes contidas no html (título, data, parágrafos, número da nota quando houver...)
  - [ ] necessidade de tratar especificamente as datas e os parágrafos de cada ano (mudança de estrutura html)
  - [ ] selecionar todas as tags importantes
  - [ ] inserir no banco de dados 
  - [ ] arquivar no internet archive
  - [ ] gerar html's


  # Integração 

- Notícias
- Agenda
- HTML

|Ministério|Notícias|Agenda|
|----------|--------|------|
|Planalto  | Específico |  Comum    |
|Casa Civil| Comum | Comum |
|MRE| Específico | Comum |
|MMA| Específico | Comum |
|Infraestrutura| Específico | Comum |
|MME| Comum | Comum |
|Economia| Comum | Sem agenda (fora do ar temporariamente) |
|Defesa| Comum | Comum |
|Saúde| Comum | |
|Ciência| Comum | |
|Mulher| Específico | |
|Comunicações| Comum | |
|Turismo| Comum | |
|Desenvolvimento Regional| Comum | |
|Biblioteca presidencia| Sem notícias | Sem agenda |
|Secretaria-Geral| Específico | |
|Controladoria-Geral da União| Específico | |
|Advocacia-Geral da União| Específico | |
|Cidadania (institucional)| Comum (>> dá problema a partir da 9ª notícia) | |  
|Cidadania (desenvolvimento social)| Específico | |
|Cidadania (esporte)| Específico | |
|Secretaria de Governo| Comum | |
|Educação| Comum | |
|Ministério da Justiça e Segurança Pública| Comum | |
|Gabinete de Segurança Institucional| Específico | |
|MAPA| Comum | |

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