salario = float(input("Dgite o salario inicial do funcionario: "))
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print(f"Salario em {i} = {salario_atual}")
