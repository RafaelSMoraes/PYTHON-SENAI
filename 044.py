#Crie um programa para jogar par ou ímpar com o usuário,e só pare quando perder.
#Ao final deve mostrar a quantidade de vitórias

import random

#correção professor
try:
    quant_vitorias = 0

    while True:
        pc = random.randint(1, 10)
        escolha = input('Par ou impar? [P/I]: ').strip().upper()[0]
        n = int(input('Numero: '))

        if ((n + pc) % 2 == 0 and escolha == 'P') or ((n + pc) % 2 != 0 and escolha == 'I'):
            print(f'{n} + {pc} = {n + pc} --> Vitoria')
            quant_vitorias +=1
        else:
            print(f'{n} + {pc} = {n + pc} --> Derrora -> Ganhou: {quant_vitorias}')
            break

except ValueError:
    print('Apenas numeros')
'''

#meu metodo não finalizado
soma = 0

maquina = random.randint(1, 10)

print(f'A maquina escolheu o numero: {maquina}')

print('----------')
j_opc = input('Qual opcao deseja?'
              '\n 1. Impar'
              '\n 2. Par'
              '\n -----------> ')

if j_opc == '1':
    print('Você escolheu IMPAR')
elif j_opc == '2':
    print('Você escolheu PAR')
else:
    print('Erro!')

j_num = int(input('Digite o numero de acordo com a opcao escolhida: '))
if j_num % 2 == 0:
    print('PAR')
else:
    print('IMPAR')

'''
