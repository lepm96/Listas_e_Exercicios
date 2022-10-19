# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
# imprima a data com o nome do mês por extenso.

data_dia = int(input('Digite o dia do seu aniversário: '))
data_mes = int(input('Digite o mês: '))
data_ano = int(input('Digite o ano: '))

print('Data de nascimento: {}/{}/{}'.format(data_dia, data_mes, data_ano))

lista_meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
               'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('Você nasceu em {} de {} de {}'.format(
    data_dia, lista_meses[data_mes], data_ano))
