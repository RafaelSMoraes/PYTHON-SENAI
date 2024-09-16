#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante

letra = input('Insira uma letra').lower().strip()[0] #lerá tudo em minusculo, não permitirá espaços no inicio
                                                     #o 0 é a forma de onde o programa começará a ler

if letra in 'aeiouáàâãéèêíìîóòõôúùû': #tudo que estiver no 'in' vai estar certo
    print(f'A {letra} é uma vogal')
else:
    print(f'A {letra} é uma consoante')

'''

Deste jeito teria erros:

if letra == 'a':
    print(f'{letra} é uma vogal')
elif letra == 'e':
    print(f'{letra} é uma vogal')
elif letra == 'i':
    print(f'{letra} é uma vogal')
elif letra == 'o':
    print(f'{letra} é uma vogal')
elif letra == 'u':
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')
'''