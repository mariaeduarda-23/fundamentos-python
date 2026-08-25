def somar_ate():
    soma = 0

    for i in range(1, numero + 1):
        soma = soma + i

    return soma

numero = int(input("Digite um número: "))
resultado = somar_ate()

print("A soma é:", resultado)

somar_ate()