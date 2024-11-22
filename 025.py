#Crie um programa para jogar JOKEMPO, usando a funcao random.randint
import random
import time

'''

#jogador

jogador = int(input('Digite um numero de 1 a 3: '))
if jogador == 1:
    print('Voce escolheu pedra')
elif jogador == 2:
    print('Voce escolheu papel')
elif jogador == 3:
    print('Voce escolheu tesoura')

#maquina

maquina = random.randint(1, 3)
if maquina == 1:
    print('Maquina escolheu pedra')
elif maquina == 2:
    print('Maquina escolheu papel')
elif maquina == 3:
    print('Maquina escolheu tesoura')

#jogo

if maquina == jogador:
    print('Empate')
elif maquina == 1 and jogador == 3:
    print('Vitoria da maquina')
elif maquina == 2 and jogador == 1:
    print('Vitoria da maquina')
elif maquina == 3 and jogador == 2:
    print('Vitoria da maquina')
else:
    print('Vitoria do jogador')
    
'''
try:
    pc = random.randint(1,3)
    j = int(input('Digite a sua escolha: '
                  '\n1- Pedra'
                  '\n2- Papel'
                  '\n3- Tesoura'
                  '\n  ----------------> '))

    print('jo')
    time.sleep(1)
    print('kem')
    time.sleep(1)
    print('PO')
    time.sleep(1)
    print('... quase la')
    if j == pc:
        print('empate')
    elif ((j == 1 and pc == 3) or
          (j == 2 and pc == 1) or
          (j == 3 and pc == 2)):
        print('Voce Ganhou!!')
    else:
        print('Voce perdeu!')

    if j == pc:
        print('empate')
    elif j == 1 and pc == 2:
        print('Computador vence ')

except ValueError:
    print('Apenas numeros')
