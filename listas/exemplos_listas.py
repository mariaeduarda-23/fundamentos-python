from entrada_dados.input import nome


def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Maria", "Larissa", "Luiz", "Rosolem", "Jaison"]
mostrar_nomes(lista_de_nomes)

# Adicionando novo nome na lista
def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nomes(lista_de_nomes, "Maria")


# Adicionando novo nome em uma posição específica
def adcionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"o nome {nome} foi inserido na posição {posicao} da lista: {nomes}")

adcionar_nome_posicao(lista_de_nomes, "rogerio", 2)

# juntando listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"os novos nomes {novos_nomes} foram inseridos na lista: {nomes}")

novos_nomes = ["francisco", "marcio"]
juntar_nomes(lista_de_nomes, novos_nomes)

# removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"o nome {nome} foi removido da lista: {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "luiz")

# Removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f'O nome da posição {posicao} é {nomes[posicao]}, foi removido!')

remover_nome_pelo_indice(lista_de_nomes)

# Descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome in nomes:
        print(f'Nome não encontrado!')
    else:
        posicao = nomes.index(nome)
        print(f'A posição do nome {nome} é {posicao}')

encontrar_posicao_pelo_valor(lista_de_nomes, nome)

# Contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f'A quantidade de nomes da lista é {quantidade}')

quantidade_de_nomes(lista_de_nomes)


# Ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenada = sorted(nomes, reverse=True)
    print(f'A lista ordenada é {lista_de_nomes_ordenada}')

ordenar_nomes(lista_de_nomes)

# Operações matemáticas
# Calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f'A média das notas é {media}')

notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, batata = gerenciar_notas(notas_semestre)
print(f'notas ordenadas: {notas_ordenadas}')
print(f'A media das notas é {batata}')
