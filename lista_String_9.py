# Verificação de CPF.
#  Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.


Tam_cpf = 14
cpf = input('Por favor, digite o CPF: ')
v1 = True  # pra não ter que usar varios prints pra verificar

if (len(cpf) != Tam_cpf):
    print('CPF informado é inválido.')
elif ((cpf[3] != ".") or cpf[7] != "." or (cpf[-3] != "-")):
    print('CPF informado é inválido.')

else:
    for i in range(Tam_cpf):
        if ((i != 3) and (i != 7) and (i != 11)):
            c = cpf[i]
            if (not c.isdigit()):
                print('CPF informado é inválido.')


if (v1):
    print('CPF informado válido.')
else:
    print('CPF informado é inválido.')
