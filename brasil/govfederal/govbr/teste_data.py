from datetime import date, timedelta, datetime

def datas():
    data_inicio = date (2019,1,1)
    data_fim = date.today()
    delta = data_fim - data_inicio
    lista_data = []
    for dia in range(delta.days+1):
        dia_delta = data_inicio + timedelta(days=dia)
        lista_data.append(dia_delta)
    lista_data_final = [datetime.strftime(dt,format="%Y-%m-%d") for dt in lista_data]
    print(lista_data_final)

def main ():
    """Função principal"""
    datas()

if __name__ == "__main__":
    main()