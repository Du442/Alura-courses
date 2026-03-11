def calculator(valor, porcentagem):
    valor_gorjeta = valor * (porcentagem / 100)
    valor_total = valor + valor_gorjeta
    
    return valor_gorjeta, valor_total