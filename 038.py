'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

import random
'''
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
'''

#correção professor:

escolha = ''


while escolha != '5':
    print('-------------------------------')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))


    escolha = input('O que deseja?\n'
                   '1 - somar\n'
                   '2 - multiplicar\n'
                   '3 - maior\n'
                   '4 - novos números\n'
                   '5 - sair do programa\n'
                   '--------->')

    if escolha == '1':
        print(f'A soma dos números são {n1 + n2 + n3}')
    elif escolha == '2':
        print(f'A multiplicação dos números são {n1*n2*n3}')
    elif escolha == '3':
        if n1 > n2 and n3:
            print(f'O maior número é {n1}')
        elif n2 > n1 and n3:
            print(f'O maior número é {n2}')
        elif n3 > n1 and n2:
            print(f'O maior número é {n3}')
    elif escolha == '4':
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        n3 = int(input('Digite um número: '))
    elif escolha == '5':
        print('Até breve')
    else:
        print('Erro!')
