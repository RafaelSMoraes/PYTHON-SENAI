# Print e Saída de Dados
'''
print('Olá Mundo')

# Operações Básicas
print(3 + 3)
print(8 - 999999)
print(898965897 / 9)
print(6 ** 24)
print(3 % 2) #resto da divisão


Idade = 45
soma_idades = 6 + 10
idade_joao = 70
idade_maria = 8
soma_joao_maria = idade_joao + idade_maria
print(soma_joao_maria)

#print formatado
print(f'A soma de idades é {soma_joao_maria}')


#Entrada de dados
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')

idade = int(input('Digite a sua idade: '))
idade_final = idade + 989
print(idade_final)


#Concatenação

Nome = 'Luis'
Sobrenome = 'Tatin'
Nome_completo = Nome + Sobrenome
print(Nome_completo)



#strings

nome = 'Rafael Moraes'

#fatiamento
print(nome[0]) #começa do primeiro caractere
print(nome[0:6]) #vai ate o setimo caractere
print(nome[5:]) #Depois do quinto caractere

#analise
print(len(nome))
print(nome.count('a')) #quantos "A" tem
print(nome.find('l')) #procura o "l" e tambem espaços ' '
print(nome.rfind('a')) #mesma coisa do anterior, mas procura apos ele

#transformação
print(nome.upper()) #transforma tudo em maiusculo
print(nome.lower()) #transforma tudo em minusculo
print(nome.capitalize()) #transforma o caractere 0 em maiusculo
print(nome.replace('l', 'oi')) #transforma o l em oi

nome = input('digite o seu nome: ').strip() #o strip só tira o espaço do antes e depois
print('nome')


#função if, elif e else

altura = 1.4

if altura > 1.3:
    print('Pode andar no briquedo')
else:
    print('quem sabe no proximo ano')

#-------------

if altura > 3:
    print('Cuidado, vai bater a cabeça')
elif altura < 3:
    print('Quem sabe ano que vem')
else:
    print('Pode andar')

#------------

nome = 'rafael moraes'

if nome == 'joao da silva'
    print('tá liberdo')
else:
    print('nome incorreto')

#biblioteca de escolhas aleatorias

import random

aleatorio = random.randint(1,10) #randit é de numeros inteiros
print(aleatorio)

#Biblioteca time

import time

print('Jo')
time.sleep(1)
print('Kem')
time.sleep(1)
print('PO')
time.sleep(1)
print('... quase laaaaa')
time.sleep(2)

print('Otario')

'''

#loops de repetição utilizando a 'for'

for ele in range (0, 10): #o 'ele' é uma variavel descartavel
    print('*')

for ele in range (10 , 0, -1 ): #Conta do maior para o menor (10 ,9, 8...)
    print(ele)

for ele in range (0, 10): #troca a variavel descartavel por numeros de forma crescente
    print(ele)

#UTILIZANDO FOR PARA SOMA E CACLUOS

#primeiro crie uma variavel
soma = 0

#crie o for, o nome da primeira variavel pouco importa
for ele in range (0, 11): #vai trocar o antigo valor pra um novo causando a sua soma
    soma = soma + ele

print(soma)
