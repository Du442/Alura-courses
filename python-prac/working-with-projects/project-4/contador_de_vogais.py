def contador_vogais(texto):
    quantidade_de_vogais = 0
    lista_de_vogais = list(texto.lower())
    for i in texto:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            quantidade_de_vogais += 1
        else:
            continue
    
    print(f'O texto contém {quantidade_de_vogais} vogais.')


# roblox = "Eu amo roblox.".lower()
# lista_de_minusculas = list(roblox)
# print(lista_de_minusculas)