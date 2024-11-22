#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
try:
    numeros = int(input('Digite um número para ter a tabuada dele: '))

    for ele in range (0, 11):
        neymar = ele * numeros
        print(f'| {ele} * {numeros} = {neymar}|')

except ValueError:
    print('Apenas numeros')
