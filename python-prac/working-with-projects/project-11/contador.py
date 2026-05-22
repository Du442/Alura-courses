cedulas = [100, 50, 20, 10, 5, 2]

def contador_cedulas_unicas():

    try:

        saque = int(input('Digite o valor do saque: \n'))
        if saque <= 0: 
            print("Erro: O valor deve ser positivo.")
        elif saque % 2 != 0: 
            print("Erro: O valor deve ser múltiplo de 2.")
        else: 
            print("Cédulas entregues:")
            for cedula in cedulas:
                quantidade = saque // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    saque = saque % cedula
    
    except ValueError as verror:
        print("Erro:", verror)