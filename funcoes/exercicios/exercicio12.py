def desconto():
    preco = float(input("Digite o preço do produto: "))
    percentual = float(input("Digite o percentual de desconto: "))

    valor_desconto = preco * percentual / 100
    valor_final = preco - valor_desconto

    print("O valor final é:", valor_final)

desconto()