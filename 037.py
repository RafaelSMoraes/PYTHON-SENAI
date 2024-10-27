#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

import random

maquina = random.randint(1, 10)
print(maquina)


escolha = ''
tentativas = 0
while escolha != maquina:
    escolha = int(input('Descubra o numero que eu estou pensando: '))
    tentativas += 1
    if escolha == maquina:
        print(f'Voce levou {tentativas} tentativas para acertar e acertou, PARABENS!!')
    else:
        print('Voce errou')