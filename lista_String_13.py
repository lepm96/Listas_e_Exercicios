# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. 
# Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.


import random

tentativa = 7
palavras = 'TESTE','PROGRAMA','SHOW','OVO','VIVAOLINUX','PYTHON','LUCAS','LINUX','LIMOSINE','FERRARI','CAMARO','BRANCO','PESQUISAR'
sorteado = random.choice(palavras)
while tentativa != 0:
    embaralha = random.sample(sorteado, len(sorteado))
    juntar_palavra_embaralhada = ''.join(embaralha)
    print(juntar_palavra_embaralhada)
    print("="*20)
    tent = input("Digite a palavra: ").upper()
    if tent == sorteado:
        print("\nParabens! Voce venceu!")
        break
    else:
        tentativa -= 1
        print("\nVoce errou! Tentativas restantes {tentativa}")
        print("="*20)
