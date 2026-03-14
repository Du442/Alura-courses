from palavras_longas import mostrar_palavras_longas

texto_digitado = input("Digite seu texto: ")
resultado = mostrar_palavras_longas(texto_digitado)

if not resultado:
    print('Nenhuma palavra longa encontrada')
else:
    print(f'Palavras longas encontradas: {resultado}')