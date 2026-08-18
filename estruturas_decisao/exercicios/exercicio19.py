def classificacao_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        classificacao = "positivo"
    elif numero < 0:
        classificacao = "negativo"
    else:
        classificacao = "zero"

    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print("Número:", numero)
    print("Classificação:", classificacao, "e", paridade)

classificacao_numero()