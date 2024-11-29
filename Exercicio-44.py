from datetime import datetime

def dias_entre_datas(data1, data2):
    formato_data = "%d/%m/%Y"
    d1 = datetime.strptime(data1, formato_data)
    d2 = datetime.strptime(data2, formato_data)
    diferenca = abs((d2 - d1).days)
    return diferenca

data1 = "01/01/2023"
data2 = "01/01/2024"
print(f"Há {dias_entre_datas(data1, data2)} dias entre {data1} e {data2}")
