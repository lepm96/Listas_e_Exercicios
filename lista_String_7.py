# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

frase = input('Digite a frase: ')

print(frase.count(' '))

for letra in frase:
    if letra in "aeiou":
        print(letra, end=' ')
