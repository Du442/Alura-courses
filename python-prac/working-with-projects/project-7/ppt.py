import random

def pedra_papel_tesoura(resposta_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_bot = random.choice(opcoes)

    # if resposta_usuario == 'pedra' and escolha_bot == 'papel':
    #     return f'\nVocê perdeu! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'pedra' and escolha_bot == 'pedra':
    #     return f'\nEmpate! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'pedra' and escolha_bot == 'tesoura':
    #     return f'\nVocê ganhou! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'papel' and escolha_bot == 'pedra':
    #     return f'\nVocê ganhou! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'papel' and escolha_bot == 'papel':
    #     return f'\nEmpate \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'papel' and escolha_bot == 'tesoura':
    #     return f'\nVocê Perdeu! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'tesoura' and escolha_bot == 'pedra':
    #     return f'\nVocê perdeu! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'tesoura' and escolha_bot == 'tesoura':
    #     return f'\nEmpate! \nO bot escolheu {escolha_bot}\n'
    # elif resposta_usuario == 'tesoura' and escolha_bot == 'pedra':
    #     return f'\nVocê Perdeu! \nO bot escolheu {escolha_bot}\n'

    if resposta_usuario not in opcoes:
        print('Resposta incorreta!')
        return
    
    print(f"Computador escolheu: {resposta_usuario}") 

    if escolha_bot == resposta_usuario:
        return f'\nEmpate!\n'
    elif ( 
        (resposta_usuario == "pedra" and escolha_bot == "tesoura") or 
        (resposta_usuario == "papel" and escolha_bot == "pedra") or 
        (resposta_usuario == "tesoura" and escolha_bot == "papel") 
    ): 
        print(f"\nVocê venceu!\n")
    else: 
        print(f"\nVocê perdeu!\n") 