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
git pull origin main && conda activate env_govlatinamerica && conda env update
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
- [ ] separar em um template a inserção no banco de dados (em andamento)
- [ ] separar em um template os apontamentos dos diretórios (em andamento)
- [ ] separar em um template o internet archive (em andamento)
- [x] salvar os arquivos no internet archive 
- [ ] otimizar importação 
- [ ] .env_dir está na pasta template_html e diretorios, e deve ficar apenas em diretorios
- [ ] ajustar link e link_archive para url e url_archive
- [ ] colocar link_archive como lista e não como str
- [ ] inserir no json a data em que o link foi salvo no internet archive
- [ ] fazer uma chamada genérica no internet archive (em andamento)
- [ ] documentar estrutura dos repositórios do gitlab


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