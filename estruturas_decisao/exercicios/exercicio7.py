def temperatura():
    celsius = float(input("Digite a temperatura em Celsius: "))

    if celsius < 15:
        print("Frio")
    elif celsius <= 25:
        print("Agradável")
    else:
        print("Quente")

temperatura()