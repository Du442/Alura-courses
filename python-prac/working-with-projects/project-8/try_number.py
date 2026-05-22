import random, os


def adivinhar_numero(entrada):

    numero_aleatorio = random.randint(1, 100)
    numero_chutado = entrada
    while numero_chutado <= 0 or numero_chutado > 100:
        print("Entrada inválida!\n")
        numero_chutado = int(input("Digite novamente um número entre 1 e 100: \n"))
    while numero_chutado != numero_aleatorio:
        if numero_chutado > numero_aleatorio:
            print("O numero é menor.")
        else:
            print("O número é maior.")
        numero_chutado = int(input("\nDigite o número que você acha que é o correto entre 1 e 100: "))
    os.system('cls')
    print(f"Você acertou o numero {numero_aleatorio}, parabéns!!!")
        
        