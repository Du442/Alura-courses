from gerador_de_senha import gerador_de_senha

gerar_senha = input('Deseja gerar uma senha aleatória? ')

if gerar_senha == 'sim' or gerar_senha == 's':
    print(gerador_de_senha())
else:
    print("Saindo...")