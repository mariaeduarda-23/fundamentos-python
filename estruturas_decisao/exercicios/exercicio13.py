def preco_ingresso():
    idade = int(input("Qual a sua idade? "))

    if   idade <= 5:
        print(f'Ingresso GRATUITO')
    elif idade <= 12:
        print(f'Ingresso: R$10,00')
    elif idade <= 59:
        print(f'Ingresso: R$20,00')
    else:
        print(f'Ingresso: R$10,00')



preco_ingresso()
