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

# Próximas atividades

## Ministério das Relações Exteriores

- [ ] coleta das notas de imprensa atuais
    - [x] entrar no link e extrair os parágrafos
    - [x] retirar parágrafos desnecessários, parágrafos em branco e caracteres /xa0
    - [ ] percorrer todas as páginas disponíveis e extrair as notas
    - [ ] inserir as informações no banco json 
    - [ ] gerar os htmls

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