
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

numeros = input('Digite os numeros separados por espaços: ').split()
numerosa = list(map(int, numeros))

for i in numerosa:
    if i % 2 == 0:
        continue
    else:
        numerosa.remove(i)
    
print(f'Números pares: {" ".join(map(str, numerosa))}')