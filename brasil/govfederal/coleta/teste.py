import os

def teste_acesso():
    print("Você acessou a pasta coleta")
    dir_atual = os.environ["PWD"] # pwd >> mostra a pasta atual em que você está
    lista_dir_atual = dir_atual.split("/")
    NOME_PROJETO = lista_dir_atual[lista_dir_atual.index("codigo")+1]
    print(NOME_PROJETO)
    lista_dir_atual_02 = dir_atual.split(NOME_PROJETO)
    dir_root = lista_dir_atual_02[0]+NOME_PROJETO
    print(dir_root)

def main():
    teste_acesso()

if __name__=="__main__":
    main()