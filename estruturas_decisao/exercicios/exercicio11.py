def imc():
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    imc = peso / (altura * altura)
    print(f"IMC: {imc}")

    if imc <= 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.5:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
        
imc()