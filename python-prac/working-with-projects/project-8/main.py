from try_number import adivinhar_numero

try:

    resposta = int(input("Digite o número que você acha que é o correto entre 1 e 100: "))

    adivinhar_numero(resposta)

except ValueError as verr:
    print(f'Entrada inválida: {verr}')