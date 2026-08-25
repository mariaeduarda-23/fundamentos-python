def somar_pares(inicio, fim):
    soma = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma = soma + i

    return soma


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

resultado = somar_pares(inicio, fim)

print("A soma dos números pares é:", resultado)