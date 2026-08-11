def consumo_energia():
    consumo = float(input("Digite o consumo em kWh: "))
    preco = float(input("Digite o preço do kWh: "))

    valor_conta = consumo * preco

    print("O valor da conta é:", valor_conta)

consumo_energia()