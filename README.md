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

- [x] documentar criação do ambiente virtual 
- [x] habilitar ambiente virtual na estação remota 
- [x] instalação do vscode 
- [x] indicar onde colocar os dados coletados 
- [ ] gerar HTMLs a partir do BD json (template construído, falta escalar)
- [ ] salvar os arquivos no internet archive 
- [ ] definir variáveis de ambiente 
- [ ] construir classes para abrigar as partes similares dos sites

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
|Biblioteca presidencia| Sem notícias | Sem agenda |
