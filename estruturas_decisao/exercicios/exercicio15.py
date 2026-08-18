def classificacao_velocidade():
    velocidade = float(input("Qual a velocidade do veículo? "))

    if   velocidade <= 60:
        print(f'Velocidade permitida')
    elif velocidade >= 61 and velocidade <= 80:
        print('Atenção: velocidade acima do permitido')
    elif velocidade > 80:
        print("Multa por excesso de velocidade")

classificacao_velocidade()