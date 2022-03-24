

# Tarefas

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

## Ministério das Relações Exteriores

- [ ] TRATAMENTO DAS NOTAS DE IMPRENSA DE 1997 A 2013
  - [ ] verificar problema de encode de 2013
  - [x] verificar todas as informações importantes contidas no html (título, data, parágrafos, número da nota quando houver...)
  - [ ] substituir as quebras de linha (\n) por espaço em cada parágrafo
  - [ ] necessidade de tratar especificamente as datas e os parágrafos de cada ano (mudança de estrutura html)
  - [ ] selecionar todas as tags importantes
  - [ ] inserir no banco de dados 
  - [ ] arquivar no internet archive nossos htmls locais
  - [ ] gerar htmls
- [ ] coleta das notas de imprensa atuais
    - [ ] entrar no link e extrair os parágrafos
    - [ ] percorrer todas as páginas disponíveis e extrair as notas
    - [ ] inserir as informações no banco json 
    - [ ] gerar os htmls