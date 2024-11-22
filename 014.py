#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo

try:
    n1 = float(input('Digite um numero para saber se ele é positivo ou negativo: '))

    if n1 > 0:
        print('o numero é positivo')
    elif n1 == 0:
        print('neutro')
    else:
        print('o numero é negativo')

except ValueError:
    print('Apenas numeros')
