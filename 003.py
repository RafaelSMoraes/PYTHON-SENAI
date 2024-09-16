#Escreva um programa que leia o nome,
#e o sobrenome, CONCATENE em uma nova variável nome completo,
#e retorne para o usuário

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

nome_completo = nome + ' ' + sobrenome

print(f'Seu nome é {nome_completo}')