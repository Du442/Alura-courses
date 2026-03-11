from calculator import calculator
try:

    valor_conta = float(input('Digite o valor da conta: '))
    porcentagem_conta = float(input('Digite a porcentagem de gorjeta: '))

    print(calculator(valor_conta, porcentagem_conta))

except ValueError as value_err:
    print('Digite um valor válido.')


