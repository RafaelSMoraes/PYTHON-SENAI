'''
Escreva um programa que peça ao usuário 5 notas
, de 0 a 10 e imprima se a média,
é insuficiente (menor que 6),
suficiente (entre 6 e 7)
, bom (entre 7 e 9)
ou excelente (9 ou maior).
'''
try:
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    n3 = int(input('Nota 3: '))
    n4 = int(input('Nota 4: '))
    n5 = int(input('Nota 5: '))

    media = (n1 + n2 + n3 + n4 + n5) / 5

    if media >= 9 :
        print('Excelente!.')
    elif media >= 8 :
        print('Bom.')
    elif media >= 6 :
        print('Suficiente.')
    else:
        print('Insuficiente')

except ValueError:
    print('Apenas numeros')
