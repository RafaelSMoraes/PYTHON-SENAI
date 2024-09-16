#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

n1 = float(input('Coloque um numero para saber se ele é par ou impar: '))

if n1 % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')