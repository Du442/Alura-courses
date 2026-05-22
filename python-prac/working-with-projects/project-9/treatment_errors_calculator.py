def calculadora_simples():
    try:

        lista_de_operacoes = ['+', '-', '*', '/']

        numero1 = int(input("Digite o primeiro número: \n"))
        operacao = input("Escolha a operação (+, -, *, /): \n")
        if operacao not in lista_de_operacoes:
            return 'Opção inválida.'
        numero2 = int(input("Digite o segundo número: "))

        if operacao == '+':
            resultado_1 = numero1 + numero2
            return f'Resultado: {resultado_1}'
        elif operacao == '-':
            resultado_2 = numero1 - numero2
            return f'Resultado: {resultado_2}'
        elif operacao == '*':
            resultado_3 = numero1 * numero2
            return f'Resultado: {resultado_3}'
        elif operacao == '/':
            resultado_4 = numero1 / numero2
            return f'Resultado: {resultado_4}'

    except ValueError:
        return 'Erro: Entrada inválida. Digite apenas números.'
    except ZeroDivisionError:
        return 'Erro: Divisão por zero não é permitida.'