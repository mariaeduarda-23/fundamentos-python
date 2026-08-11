def comissao():
    salario_fixo = float(input("Digite o salário fixo: "))
    vendas = float(input("Digite o valor das vendas: "))
    percentual = float(input("Digite o percentual de comissão: "))

    comissao = vendas * percentual / 100
    salario_final = salario_fixo + comissao

    print("O salário final é:", salario_final)

comissao()