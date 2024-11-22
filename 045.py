#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

try:
    while True:
        numeros = input('Digite um número para ter a tabuada dele: ')

        for ele in range (0, 11):
            print(f'{numeros} X {ele} = {int(numeros) * ele}')

        if numeros == '0000':
            print('Serviço finalizado.')
            break
except ValueError:
    print('Apenas numeros')