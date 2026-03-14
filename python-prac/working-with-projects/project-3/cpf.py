def verificar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."
        
    # Meu jeito de fazer:         
    #     cpf_caracteres = list(str(cpf))
    #     for i in range(0, len(cpf_caracteres)):
    #         if len(cpf_caracteres) == 11 and type(cpf_caracteres[i]) == str:
    #             return f'CPF Válido.'
    #         else:
    #             return f'CPF Inválido.'
    # except ValueError as value_err:
    #     print('ERRO! O CPF deve conter apenas números.')
# cpf_teste = 22222222222

# print(verificar_cpf(cpf_teste))