# Coleta de Dados de sites governamentais da América Latina

## Informações Importantes

| Conteúdo           | Link de Acesso                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| Código das Coletas | [Repositório GitLab](https://gitlab.com/unesp-labri/projeto/govlatinamerica)                       |
| Informações gerais | [Pasta Google Drive](https://drive.google.com/drive/u/1/folders/1_g01RcccLl2PpTupxQyCoXEJka30VXeG) |
| Tarefas do projeto | [Notion](https://www.notion.so/Projeto-GovLatinAmerica-9219a9b60ae24cb98a197f7bdab42209)           |
| Documentação       | [Site](https://apoio.labriunesp.org/docs/projetos/dados/gov-latin-america/intro/)                  |



# sincronizar com o gitlab (na pasta raiz GOVLATINAMERICA)

```
git add .
git commit -m "comentário"
git pull origin main
git push origin main
```

# verificar atualizações do ambiente virtual

```
git pull origin main && conda activate env_govlatinamerica && conda env update
```

# Pendencias

- documentar criação do ambiente virtual - OK
- habilitar ambiente virtual na estação remota - OK
- instalação do vscode - OK
- indicar onde colocar os dados coletados - OK

# Integração 

- Notícias
- Agenda
- HTML

|Ministério|Notícias|Agenda|
|----------|--------|------|
|Planalto  | Específico |      |
|Casa Civil| Comum | |
|MRE| Específico | |
|MMA| Específico | |
|Infraestrutura| Específico | |
|MME| Comum | |
|Economia| Comum | |
|Defesa| Comum | |
|MAPA| Comum | |
|Biblioteca presidencia| Sem notícias | |
