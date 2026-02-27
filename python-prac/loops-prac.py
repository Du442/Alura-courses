# first exercise

# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

# for cliente in clientes:
#     print(f'Nome: {cliente}')

# secord exercise

# contador = 0

# while contador < 10:
#     if contador == 9:
#         print('Sucesso!')
#     else:
#         print('Em processamento...')
#     contador += 1

# # third exercise

# mensagem = 'Bem-vindo ao Buscante!'
# vezes = int(input('Digite a quantidade de vezes que a mensagem sera exibida: '))
# contador = 0

# while contador < vezes:
#     print(mensagem)
#     contador += 1

# fourth exercise

# valores = [10, 20, 30, 40, 50]

# soma_de_valores = sum(valores)
# print(f'A soma dos valores é: {soma_de_valores}')

# fifth exercise

# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for p in projetos:
#     if p is None:
#         print('Projeto ausente.')
#         continue
#     print(f'{p}')

# sixth exercise

# livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

# livro_procurado = str(input('Digite o nome do livro que deseja buscar: '))

# for livro in livros:
#     if livro == livro_procurado:
#         print('Livro encontrado.')
#         break
#     print(f'Livro: {livro}')

# seventh exercise

# estoque = 5

# pergunta = str(input('Deseja comprar um produto? (s/n): '))

# while pergunta == 's' and estoque > 0:
#     print('Produto comprado com sucesso!')
#     estoque -= 1
#     pergunta = str(input('Deseja comprar um produto? (s/n): '))
#     if pergunta == 'n':
#         print('Compra cancelada!')
#         break
# else:
#     print('Produto esgotado!')

# eighth exercise

# contador = 10

# while contador >= 1:
#     if contador % 2 == 0:
#         print(f'Faltam apenas {contador} segundos - Não perca essa oportunidade!')
#     else:
#         print(f'A contagem continua: {contador} segundos restantes.')
#     contador -= 1

# print('Aproveite a promoção agora!')

# ninth exercise

# livros = [
#     {"nome": "1984", "estoque": 5},
#     {"nome": "Dom Casmurro", "estoque": 0},
#     {"nome": "O Pequeno Príncipe", "estoque": 3},
#     {"nome": "O Hobbit", "estoque": 0},
#     {"nome": "Orgulho e Preconceito", "estoque": 2}
# ]

# for livro in livros:
#     if livro["estoque"] != 0:
#         print(f'Livro disponivel: {livro['nome']}')
#     else:
#         continue

# tenth exercise

# while True:
#     nome_usuario = input("Digite seu nome de usuário: ")
#     senha = input("Digite sua senha: ")

#     if len(nome_usuario) < 5:
#         print("O nome de usuário deve ter pelo menos 5 caracteres.")
#         continue

#     if len(senha) < 8:
#         print("A senha deve ter pelo menos 8 caracteres.")
#         continue

#     print("Cadastro realizado com sucesso!")
#     break