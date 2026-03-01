import re

# first exercise

# nome = input('Digite o nome do produto: ')

# print(nome.lower().strip())

# second exercise

# nome = input('Digite o nome do cliente: ')
# cidade = input('Digite o nome da sua cidade: ')

# print(f'Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}')

# third exercise

# palavra = input('Digite uma palavra-chave: ')

# print(f'Primeiras 3 letras: {palavra[:3]}')
# print(f'Ultimas 3 letras: {palavra[-3:]}')
# print(f'Todas as letras: {palavra}')

# fourth exercise

# url = input('Digite a url para a validação: ')

# if url.startswith('https://') and url.endswith('.com'):
#     print('URL valida!')
# else:
#     print('URL invalida!')

# fifth exercise

# texto = input("Digite a descrição da receita: ")  
# numero = re.findall(r'\d+', texto)[0]  
# print(f"O número da receita é: {numero}")

# sixth exercise

# texto_revisao = 'Digite o texto para ser revisado: O dia está bom, tudo está bom.'
# print(texto_revisao)
# nova_palavra = input('Digite a palavra para ser substituida: ')
# qual_palavra = input('Digite a palavra nova: ')

# texto_final = re.sub(rf'\b{nova_palavra}\b', qual_palavra, texto_revisao)
# print(texto_final)

# seventh exercise

# nome = input("Digite o nome do cliente para validação: ")  
# if re.fullmatch(r'[A-Z][a-z]*', nome):
#     print("Nome válido!")
# else:
#     print("Nome inválido!")

# eighth exercise

# cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
# padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

# if re.search(padrao, cpf):
#     print("O CPF está no formato correto.")
# else:
#     print("O CPF está no formato incorreto.")

# ninth exercise

# texto = input("Digite o título dos livro: ") 
# letra = input("Digite a letra inicial para pesquisa: ")  
# palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)
# print(palavras)

# tenth exercise

# dados = input("Digite o nome completo e o ano de nascimento do paciente: ")  
# padrao = r'(\w+) (\w+) - (\d{4})'  

# resultado = re.search(padrao, dados)

# if resultado:
#     primeiro_nome = resultado.group(1)
#     sobrenome = resultado.group(2)
#     ano_nascimento = resultado.group(3)

#     print(f"Primeiro Nome: {primeiro_nome}")
#     print(f"Sobrenome: {sobrenome}")
#     print(f"Ano de Nascimento: {ano_nascimento}")
# else:
#     print("Formato inválido!")