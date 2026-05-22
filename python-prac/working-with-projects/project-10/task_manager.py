import os

validacao = [1,2,3,4]
lista = []

def task_manager():
    
    try:
        while True:
            os.system('cls')
            print('''
1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair
            ''')
            opcao_escolhida = int(input("Escolha uma opção: \n"))
            
            if opcao_escolhida == 1:
                tarefa_adicionar = input("\nDigite a tarefa: \n").lower()
                if tarefa_adicionar == '':
                    print('Digite uma tarefa válida.\n')
                    input("Digite para continuar: ")
                else:
                    lista.append(tarefa_adicionar)
                    print('\nTarefa adicionada!\n')
                    input('Digite para prosseguir: ')
            elif opcao_escolhida == 2:
                print('\nTarefas:\n')
                for i in lista:
                    print(f'{lista.index(i)}. {i}')
                input('\nDigite para prosseguir: ')
            elif opcao_escolhida == 3:
                tarefa_remover = input("\nDigite a tarefa a ser removida: \n").lower()
                for i in lista:
                    if tarefa_remover == i:
                        lista.remove(tarefa_remover)
                        print(f'Tarefa {tarefa_remover} removida!')
                        input('\nDigite para prosseguir: ')
                    else:
                        print('Erro: Nenhuma tarefa para remover.')
                        input('\nDigite para prosseguir: ')
            elif opcao_escolhida == 4:
                os.system('cls')
                print('Saindo do gerenciador de tarefas. Até mais')
                break
            else:
                os.system('cls')
                print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
                input('Digite para prosseguir: ')


    except ValueError:
        os.system('cls')
        return 'Erro! Digite um número válido.'