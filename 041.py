#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores


try:
    opcao = ''
    soma = 0
    quant = 0
    maior = None
    menor = None

    while opcao != 'sair':
        n = int(input('Número: '))
        if maior == None and menor == None:
            maior = n
            menor = n

        if n > maior:
            maior = n
        if n < menor:
            menor = n

        #Soma
        soma += n
        #Quant_Ciclos
        quant += 1

        opcao = (input('Deseja continuar? [escreva: "sair" para parar]: '))


    print(f'A média é {soma/quant}\n'
          f'O maior é {maior}\n'
          f'O menor é {menor}')

except ValueError:
    print('Apenas numeros')