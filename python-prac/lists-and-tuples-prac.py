# first exercise

# lista = ['acucar', 'sal', 'vinagre']

# item_pesquisar = input('Digite o item que você quer verificar: ')

# print(f'{item_pesquisar in lista}')

# second exercise

# notas = [85, 70, 90, 60, 75]
# notas.sort()

# print(f'Notas ordenadas: {notas}')

# third exercise

# lista_de_voluntarios = []
# answer = str(input('Digite o nome do voluntário (ou sair para encerrar): '))

# while answer != 'sair':
#     lista_de_voluntarios.append(answer)
#     answer = str(input('Digite o nome do voluntário (ou sair para encerrar): '))

# print(lista_de_voluntarios)

# fourth exercise

# produtos_estoque1 = input("Digite o produto do estoque 1 separados por virgulas: ").strip()
# produtos_estoque2 = input("Digite o produto do estoque 2 separados por virgulas: ").strip()

# estoque_final = (f'{produtos_estoque1 + ", " + produtos_estoque2}')

# print(estoque_final)

# fifth exercise

# lista = ['Ana', 'Pedro', 'Carlos']

# convidado_novo = input('Digite o novo do novo convidado: ')
# posicao = int(input('Digite a posição na qual deseja a inserir o convidado: '))

# lista.insert(posicao, convidado_novo)
# print(f'lista atualizada: {lista}')

# sixth exercise

# eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
# lista_nova = []

# for elemento in eventos_registrados:
#     if elemento == 'Abertura':
#         lista_nova.insert(0, elemento)
#     elif elemento == 'Palestra 2':
#         lista_nova.insert(0, elemento)
#     elif elemento == 'Palestra 3':
#         lista_nova.insert(0, elemento)
#     elif elemento == 'Encerramento':
#         lista_nova.insert(3, elemento)
#     else:
#         print('erro!')

# print(lista_nova)

# seventh exercise

# lista_atual = ['Ana', 'Carlos', 'Pedro']

# nome_incorreto = str(input('Digite o nome incorreto: '))
# nome_correto = str(input('Digite o nome correto: '))


# for i in lista_atual:
#     if i == nome_incorreto:
#         posicao = lista_atual.index(nome_incorreto)
#         lista_atual.pop(posicao)
#         lista_atual.insert(posicao, nome_correto)

# print(f'''\nO nome de {nome_incorreto} foi alterado para {nome_correto}. \n
# Lista atualizada para: {lista_atual}
# ''')


# e

# pedidos = str(input('Digite quais os pedidos feitos (Separe entre espaços): '))

# lista_de_pedidos = pedidos.split()

# pedidos_final = str(input('Deseja remover o ultimo pedido da lista? s/n '))
# if pedidos_final == 's':
#     lista_de_pedidos.pop(-1)
# elif pedidos_final == 'n':
#     print('Nenhum produto removido!')
# else:
#     print('Não entendi.')

# print(lista_de_pedidos)

# ninth exercise

# notas = input('Digite as notas separadas por espaços: ')
# lista_de_strings = notas.split()
# lista_de_notas = list(map(int, lista_de_strings))

# calculo_media = sum(lista_de_notas) / len(lista_de_notas)

# print(round(calculo_media, 2))

# tenth exercise

# dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(", ")

# for i in range(0, len(dados), 3):
#     nome, idade, nota = dados[i], int(dados[i+1]), float(dados[i+2])
#     print(f'\nNome: {nome}')
#     print(f'Idade: {idade}')
#     print(f'Nota: {nota}\n')