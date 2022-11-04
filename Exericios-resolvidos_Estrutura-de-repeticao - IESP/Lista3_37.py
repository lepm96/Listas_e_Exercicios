cod_clientes = []
altura_clientes = []
peso_clientes = []
n_cliente = 1
codigo = True

while codigo != 0:
    print(f"\nCliente n° {n_cliente}")
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        n_cliente += 1

cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(max(altura_clientes))
cod_baixo = altura_clientes.index(min(altura_clientes))
print("\n" * 5)
print(f"Código do mais magro: {cod_clientes[cod_magro]}")
print(f"Código do mais gordo: {cod_clientes[cod_gordo]}")
print(f"Código do mais alto: {cod_clientes[cod_alto]}")
print(f"Código do mais baixo: {cod_clientes[cod_baixo]}")
print(f"Média de altura: {sum(altura_clientes) / len(altura_clientes)}")
print(f"Média de peso: {sum(peso_clientes) / len(peso_clientes)}")
