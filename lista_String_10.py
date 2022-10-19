# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
from unicodedata import numeric


numero = int(input('Digite um número de 0 a 99: '))

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')  # até 99... mesma lógica.

if 0 <= numero <= 99:
    print(f'Você digitou o número {cont[numero]}')
else:
    print('Você digitou um número inválido')
