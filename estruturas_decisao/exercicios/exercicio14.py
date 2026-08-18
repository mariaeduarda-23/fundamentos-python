def sistema_votacao():
    idade = int(input("Qual a sua idade? "))

    if   idade < 16:
        print(f'Não pode votar')
    elif idade >= 16 and idade <= 17:
        print("Voto Opcional")
    elif idade >= 18 and idade <= 69:
        print("Voto Obrigatorio")
    elif idade >= 70:
        print("Voto Opcional")
        
sistema_votacao()