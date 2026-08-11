def consumo():
    distancia = float(input("Digite a distância percorrida: "))
    combustivel = float(input("Digite a quantidade de combustível: "))

    consumo_medio = distancia / combustivel

    print("O consumo médio é:", consumo_medio, "km/L")

consumo()