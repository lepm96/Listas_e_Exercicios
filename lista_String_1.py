# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
f1 = (input('Digite a 1ª frase: '))
f2 = (input('Digite a 2ª frase: '))


print('Tamanho de "', f1, '":', len(f1), ' caracteres.')
print('Tamanho de "', f2, '":', len(f2), ' caracteres.')


if f1 == f2:
    print('As duas Strings possuem o mesmo conteúdo.')
elif f1 != f2:
    print('As duas Strings possuem conteúdos diferentes.')


if (len(f1) == len(f2)):
    print('As duas String são do mesmo tamanho.')
else:
    print('As duas String são de tamanhos diferentes.')
