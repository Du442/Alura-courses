# First exercise

# resposta = ''
# conjunto = set()

# while resposta != "sair":
#     resposta = input('Digite o nome do convidado: ')
#     if resposta.lower() == 'sair':
#         break
#     conjunto.add(resposta)

# print(f'Convidados confirmado: {conjunto}')

#second exercise

# conjunto1 = set(input(('texto 1: ').lower().split(' ')))
# conjunto2 = set(input(('texto 2: ').lower().split(' ')))

# intersection = conjunto1 & conjunto2

# print(intersection)

# third exercise

# lista_de_laura = set(input('Lista de Laura: ').split(' '))
# lista_de_ana = set(input('Lista de Ana: ').split(' '))

# contidos_nos_dois = lista_de_laura & lista_de_ana
# diferenca_1 = lista_de_laura - lista_de_ana
# diferenca_2 = lista_de_ana - lista_de_laura

# print(f"""\nItens em ambas as listas: {contidos_nos_dois}\n
# Itens exclusivos de Laura: {diferenca_1}\n
# Itens exclusivos de Ana: {diferenca_2}\n""")

# fourth exercise

# permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 
# permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

# for i in range(len(permissoes_principais)):  

#     permissoes_principais[i] = permissoes_principais[i].strip() 

# for i in range(len(permissoes_solicitadas)):  

#     permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

# eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 

# if eh_subconjunto:  

#     print("As permissões solicitadas fazem parte das permissões principais.")  

# else:  

#     print("As permissões solicitadas não fazem parte das permissões principais.") 

# fiventh exercise

# equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

# equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

# uniao_das_equipes = equipe_a | equipe_b
# print(uniao_das_equipes)

# elementos_removidos = int(input('Deseja remover quantos elementos? '))

# for i in range(0, elementos_removidos):
#     print(f'\n {uniao_das_equipes}')
#     resposta = input('Qual elemento deseja remover: ')
#     if resposta in uniao_das_equipes:
#         uniao_das_equipes.remove(resposta)
#         print(f'\n Item removido com sucesso')
#     else:
#         print('O item não existe dentro dessa união')
#         continue

# print(f'\nTodos os itens solicitados foram removido com êxito!')

# sixth exercise

# dictionary = {}

# for i in range (0, 3):
#     nome_produto = input('\nDigite o nome do produto: ')
#     valor_produto = int(input('\nDigite o valor do produto: '))
#     dictionary.update({nome_produto:valor_produto})
    
# print(f'Dicionário de produtos: {dictionary}')

# seventh exercise


# estoque = { 

#     "Caderno universitário": 50, 

#     "Caneta azul": 120, 

#     "Borracha branca": 30 

# } 

# print(f'{estoque}\n')
# produto_atualizado = input(f'\nDigite o nome do produto a ser atualizado: ')
# nova_quantidade = int(input(f'\nDigite a nova quantidade do produto: '))
# estoque.update({produto_atualizado:nova_quantidade})

# print(estoque)

# eighth exercise


# participantes = { 

#     "Mariana": 25, 

#     "Carlos": 32, 

#     "Beatriz": 28, 

#     "Rafael": 35 

# }

# print(f"Nomes dos participantes: {', '.join(participantes.keys())}") 

# print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}") 

# print("Participantes e suas idades:") 

# for nome, idade in participantes.items(): 

#     print(f"- {nome}: {idade} anos") 

# ninth exercise

# participantes = { 

#     "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

#     "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

# }

# participante_removido = input('Digite o participante a ser removido: ')

# for workshop, nomes in participantes.items():
#     nomes.discard(participante_removido)

# for workshop, nomes in participantes.items(): 
#     print(f"{workshop}: {nomes}")

# tenth exercise


# vendas = { 

#     "Eletrônicos": [ 

#         {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

#         {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

#     ], 

#     "Eletrodomésticos": [ 

#         {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

#         {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

#     ], 

#     "Livros": [ 

#         {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

#         {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

#     ] 

# }

# for categoria, items in vendas.items():
#     total = 0
#     for item in items:
#         total += item['quantidade'] * item['valor_unitario']
#     print(f"- {categoria}: R$ {total:.2f}")