def jogo_adivinhacao(numero_secreto):
    palpite = int(input("Digite seu palpite: "))

    while palpite != numero_secreto:
        if palpite > numero_secreto:
            print("O palpite é maior que o número secreto.")
        else:
            print("O palpite é menor que o número secreto.")

        palpite = int(input("Tente novamente: "))

    print("Parabéns! Você acertou!")


numero_secreto = 7
jogo_adivinhacao(numero_secreto)