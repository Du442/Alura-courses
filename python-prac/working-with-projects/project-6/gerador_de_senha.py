import random as rd

def gerador_de_senha():

    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
    
    password = [
        rd.choice(maiusculas),
        rd.choice(minusculas),
        rd.choice(numeros),     
        rd.choice(especiais)    
    ]

    todos_caracteres = maiusculas + minusculas + numeros + especiais
    password.extend(rd.choices(todos_caracteres, k=8))
    rd.shuffle(password)
    return ''.join(password)

