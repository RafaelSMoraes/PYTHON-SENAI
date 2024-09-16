#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

n1 = float(input('Insira um numero:'))
n2 = float(input('Insira outro numero: '))

if n1 == n2:
    print(f'{n1} é igual a {n2}')
else:
    print(f'{n1} é diferente de {n2}')