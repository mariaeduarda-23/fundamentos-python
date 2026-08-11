def conversao_idade():
    idade = int(input("Digite sua idade em anos: "))

    meses = idade * 12
    dias = idade * 365

    print("Você tem aproximadamente", meses, "meses.")
    print("Você tem aproximadamente", dias, "dias.")

conversao_idade()