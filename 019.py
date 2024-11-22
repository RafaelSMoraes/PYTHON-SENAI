#Escreva um programa que peça ao usuário um número e
#imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.
try:
    numero = int(input('Insira um numero: '))

    if numero > 20:
        print(f'O {numero} esta maior que vinte')
    elif numero > 10:
        print(f'O {numero} esta entre 10 e 20')
    elif numero > 0:
        print(f'O {numero} esta entre 0 e 10')
    else:
        print('Menor que 0')

except ValueError:
    print('Apenas numeros')

#resolução 2
'''
try:
    if numero > 0 and numero < 10:  #and é o 'e' esta entre, coisas assim...
        print('Entre 0 e 10')
    elif numero > 10 and numero <20:
        print('Entre 10 e 20')
    else:
        print('Maior que 20')
        
except ValueError:
    print('Apenas numeros')
'''
