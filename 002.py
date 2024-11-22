#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário
try:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade_nascimento = input('Digite sua cidade de nascimento: ')

    print(f'Meu nome é {nome}, tenho {idade} anos e nasci em {cidade_nascimento}')
except ValueError:
    print('Apenas numeros')
