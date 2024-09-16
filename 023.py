#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

palavra = input('Digite uma palavra: ').lower().strip()[0]

if palavra in 'aeiouáàâãéèêíìîóòõôúùû': #tudo que estiver no 'in' vai estar certo
    print('Começa com uma vogal')
else:
    print('Começa com uma consoante')