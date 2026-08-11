def troca_valores():
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    print("Antes:")
    print("A =", a)
    print("B =", b)

    a, b = b, a

    print("Depois:")
    print("A =", a)
    print("B =", b)

troca_valores()