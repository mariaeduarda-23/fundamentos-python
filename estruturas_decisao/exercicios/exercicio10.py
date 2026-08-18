def desconto():
    valor = float(input("Qual o valor da compra: "))

    if valor <= 100:
        desconto= 0
    elif valor <= 500:
        desconto= 10
    else:
        desconto= 15

    valor_final = valor - (valor * desconto / 100)

    print(f'Desconto: {desconto}')
    print(f'Valor final: {valor_final}')

desconto()
