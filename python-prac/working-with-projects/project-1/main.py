from contador import *

frase = input("Digite uma frase: ").strip()
if not frase:
    print('Erro! Nenhuma frase foi digitada aqui.')
else:
    resultado = contar_palavras(frase)
    if resultado:
        print(f'Contagem de palavras:')
        for palavra, quantidade in resultado.items():
            print(f'{palavra}:{quantidade}')
    else:
        print('Nenhuma palavra válida foi encontrada!')