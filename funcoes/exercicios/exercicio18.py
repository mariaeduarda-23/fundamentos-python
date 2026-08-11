def prestacao():
    valor = float(input("Digite o valor do produto: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))

    valor_parcela = valor / parcelas

    print("O valor de cada parcela é:", valor_parcela)

prestacao()