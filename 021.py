#Escreva um programa que peça ao usuário um número de
#1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).
'''
d1 = 'SEGUNDA-FEIRA'
d2 = 'TERÇA-FEIRA'
d3 = 'QUARTA-FEIRA'
d4 = 'QUINTA-FEIRA'
d5 = 'SEXTA-FEIRA'
d6 = 'SÁBADO'
d7 = 'DOMINGO'
'''

user = int(input('Coloque um numero de 1 a 7 para saber o dia da semana: '))

if user == 1:
    print('Segunda-Feira')
elif user == 2:
    print('Terça-Feira')
elif user == 3:
    print('Quarta-Feira')
elif user == 4:
    print('Quinta-Feira')
elif user == 5:
    print('Sexta-Feira')
elif user == 6:
    print('Sábado')
elif user == 7:
    print('Domingo')
else:
    print('Esse número não consta na nossa base de dados, tente novamente')
