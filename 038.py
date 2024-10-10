'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

import random

opcao = ''
while opcao != 'Sair':
    numero = []
    for i in range (3):
        n1 = int(input('Numero: '))
        n2 = int(input('Numero: '))
        n3 = int(input('Numero: '))

        opcao = input('O que deseja?'
                  '\n1 - Somar'
                  '\n2 - Multiplicar'
                  '\n3 - Maior'
                  '\n4 - Novos numeros'
                  '\n5 - Sair ----> ')

        if opcao == '1':
            print(f'A soma  é {n1 + n2 + n3}')
        elif opcao == '2':
            print(f'A multiplicação é {n1 * n2 * n3}')
        elif opcao == '3':
            maior_numero = numero[0] #começa pelo primeiro elemento
            for num in numero [1:]: #começa da segunda posição
                if num > maior_numero:
                    maior_numero = num
            print(f'O maior número é {maior_numero}')
        elif opcao == '4':
            print('Digite novos numeros: ')
        else:
            print('Você saiu')
            exit()
