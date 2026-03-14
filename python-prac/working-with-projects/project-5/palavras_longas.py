def mostrar_palavras_longas(texto):
    palavras_separadas = texto.split()        
    lista_palavras_maiores = []
    for i in palavras_separadas:
        if len(i) > 10:
            lista_palavras_maiores.append(i)

    return lista_palavras_maiores



# texto = input('Digite seu texto aqui: ')
# palavras_separadas = texto.split()
# lista_palavras_maiores = []

# print(palavras_separadas)