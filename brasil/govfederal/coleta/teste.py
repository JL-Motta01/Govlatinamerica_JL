import os

def teste_acesso():
    print("Você acessou a pasta coleta")
    dir_atual = os.environ["PWD"] # pwd >> mostra a pasta atual em que você está
    dir_tmp = dir_atual.split("govlatinamerica")
    dir_root = dir_tmp[0]+"govlatinamerica"
    print(dir_root)

def main():
    teste_acesso()

if __name__=="__main__":
    main()