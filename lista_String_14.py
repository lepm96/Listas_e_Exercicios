#Faça um programa que peça uma texto e transforme-o para a grafia leet speak.


texto = input("Insira o texto a ser traduzido: ")
texto = texto.replace("a", "4")
texto = texto.replace("A", "4")
texto = texto.replace("e", "3")
texto = texto.replace("E", "3")
texto = texto.replace("i", "1")
texto = texto.replace("I", "1")
texto = texto.replace("o", "0")
texto = texto.replace("O", "0")
texto = texto.replace("t", "7")
texto = texto.replace("T", "7")
texto = texto.replace("s", "5")
texto = texto.replace("S", "5")
texto = texto.replace("l", "1")
texto = texto.replace("L", "1")
print(texto)