def salario():
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    horas = float(input("Digite a quantidade de horas: "))

    salario = valor_hora * horas

    print("O salário é:", salario)

salario()