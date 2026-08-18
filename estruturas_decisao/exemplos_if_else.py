def aluno_aprovado():
    nota_1 = float(input('Digite sua primeira nota: '))
    nota_2 = float(input('Digite sua segunda nota: '))

    media = (nota_1 + nota_2) / 2
    print(f'Amedia do aluno: {media}')

    if media >= 6:
        print('Aluno aprovado!')
    elif media >= 5 and media < 6:
        print('Aluno reprovado!')
    else:
        print('Aluno reprovado!')

aluno_aprovado()






def login():
    email = "maria@gmail.com"
    senha = "1234"
    codigo_secreto = "#456@"

    email_input = input('Digite seu email: ')
    senha_input = input('Digite sua senha: ')

    if email_input == email and senha_input == senha:
        print("Usuario logado!")
        acessar_admin = input('Deseja acessar o administrador? [S/N]')
        if acessar_admin == 'S':
            codigo_secreto_input = input('Digite seu codigo secreto: ')
            if codigo_secreto_input == codigo_secreto:
                print('Acesso Adm Liberado!')
            else:
                print('Codigo secreto errado!')
        elif acessar_admin == 'N':
            print('Ok. Você acessou como usuario comum!')
        else:
            print('Opção invalida!')
    else:
        print("email ou senha incorreto!")

login()
