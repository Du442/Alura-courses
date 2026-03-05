
# first exercise

# def calcular_idade(ano_nascimento, ano_atual): 
#     return ano_atual - ano_nascimento 
 
# nascimento = int(input("Digite o ano de nascimento: ")) 
# atual = int(input("Digite o ano atual: ")) 
# idade = calcular_idade(nascimento, atual) 
# print(f"A idade é {idade} anos.") 

# second exercise

# def contador_de_caracteres(palavra_digitada):
#     return len(palavra_digitada)

# palavra = str(input('Digite sua palavra: '))

# print(f'Essa palavra tem {contador_de_caracteres(palavra)} caracteres.')

# third exercise

# def saudacao_horario(horario):
#     if 0 <= horario < 5:
#         return f'Boa madrugada!'
#     elif 5 <= horario < 12:
#         return f'Bom dia!'
#     elif 12 <= horario <= 18:
#         return f'Boa tarde!'
#     elif 18 < horario <= 24:
#         return f'Boa noite'
#     else:
#         return f'Erro!'
    
# horas = int(input('Digite o horário de acesso: '))

# print(saudacao_horario(horas))

#fourth exercise

# def conversao_para_inteiro(numeros):
#     """Recebe uma lista de strings numéricas e devolve uma lista de inteiros."""
#     return [int(num) for num in numeros]


# def confirmar_inteiro(numeros):
#     """Retorna True se todos os itens da lista forem inteiros, caso contrário False."""
#     for num in numeros:
#         if not isinstance(num, int):
#             return 'Erro na conversão.'
#     return 'Todos os itens da lista são inteiros.'    


# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

# telefones_int = conversao_para_inteiro(telefones)        # lista já convertida para int   # False (lista original é de strings)
# print(confirmar_inteiro(telefones_int))  # True (lista convertida é de ints)

# fourth exercise(corrigido)

# def converter_telefones(lista):  

#    return [int(telefone) for telefone in lista] 

# def verifica_tipos(lista):  

#    for num in lista:  

#        if not isinstance(num, int):  

#            return "Erro na conversão."  

#    return "Todos os números foram convertidos corretamente!" 

# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

# telefones_convertidos = converter_telefones(telefones) 

# print(verifica_tipos(telefones_convertidos)) 

# fifth exercise

# valores = input("Digite os valores das vendas: ").split() 
# total = sum(map(float, valores)) 
# print(f"O total de vendas foi: {total}") 

# sixth exercise

# numeros = input('Digite os numeros separados por espaços: ').split()
# numerosa = list(map(int, numeros))

# for i in numerosa:
#     if i % 2 == 0:
#         continue
#     else:
#         numerosa.remove(i)
    
# print(f'Números pares: {" ".join(map(str, numerosa))}')

# seventh exercise

# def transformador_de_listas(lista1, lista2):
#     dict_para_retorno = {}
#     dict_para_retorno = list(zip(lista1, lista2))
#     for produto in dict_para_retorno:
#         print(f'{produto[0]}: {produto[1]}')
#     return dict_para_retorno
    
# produtos = input('Digite os produtos separados por espaços: ').split()
# precos = input('Digite os precos separados por espaços: ').split()

# transformador_de_listas(produtos, precos)

# eighth exercise

# def calculadora(num1, num2, operacao):
#     try:
#         if operacao == '+':
#             result_case_1 = num1 + num2
#             return f'O resultado foi {result_case_1}'
#         elif operacao == '-':
#             result_case_2 = num1 - num2
#             return f'O resultado foi {result_case_2}'
#         elif operacao == '*':
#             result_case_3 = num1 * num2
#             return f'O resultado foi {result_case_3}'
#         elif operacao == '/':
#             result_case_4 = num1 / num2
#             return f'O resultado foi {result_case_4}'
#     except ZeroDivisionError as err:
#         print(f'O erro foi encontrado como {err}')
#     except TypeError as er:
#         print(f'O erro encontrado foi {er}')
#     except Exception as erro:
#         print(f'O erro encontrado foi {erro}')

# number1 = int(input('Digite o primeiro numero: '))
# number2 = int(input('Digite o segundo numero: '))
# operation = input('Digite qual operação deseja (| + | - | * | / |): ')

# print(calculadora(number1, number2, operation))

# ninth exercise

# def aplicador_desconto(valor, desconto):
#     try:
#         porcentagem = valor * (desconto / 100)
#         preco_final = valor - porcentagem
#         return preco_final
#     except ZeroDivisionError as err:
#         print(f'O erro encontrado foi: {err}')
#     except TypeError as er:
#         print(f'O erro encontrado foi: {er}')
#     except Exception as erro:
#         print(f'O erro encontrado foi: {erro}')

# porcentagem_desconto = int(input('Digite a porcentagem do desconto: '))
# valor_compra = float(input('Digite o valor total da compra: '))

# print(aplicador_desconto(valor_compra, porcentagem_desconto))

# tenth exercise

# def recursiva(n):
#     if n <= 0:
#         print('Erro')
#     else:
#         total = 0
#         while n > 0:
#             soma = n + n
#             total = total + soma
#             n -= 1
#         return total

# num = int(input('Digite um numero que você quer que retorne de forma recursiva: '))

# print(recursiva(num))