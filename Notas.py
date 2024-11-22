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

print (nome [:: -1] #inverte a palavra, se utiliza para verificação de palindromo

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



#loops de repetição utilizando a 'for'

for ele in range (0, 10): #o 'ele' é uma variavel descartavel
    print('*') #saida esperada: * * * * * * * * * * *  * (todos na vertical)

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


#descobrir palindromos

palavra = input('Digite uma palavra para saber se ela é ou não um palindromo: ').lower().strip()

if ' ' in palavra:
    palavra = palavra.replace(' ', '') #tira os espaços e pode ser utilizado textos

for palindromo in palavra:
    if palavra == palavra[:: -1]:
        print('é palindromo')
    else:
        print('não é palindromo')



#funcao 'while', o famoso enquanto


contador = 0
resposta = 'S'

while resposta != 'N' :  # condição de parada
    print(f'O contador é {contador}')
    contador += 1
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]

print('Loop concluído!')


#caso1

contador = 0

while contador < 100:
    contador += 1
    print('*') #retorna o asterisco cem vezes

#caso2
#tomada de decisão
#Diferente de (!=)
#o codigo so para se voce digitar 'N'

decisao = ''
while decisao != 'N':
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        print('é par')
    decisao = input('Deseja continuar? [S/n]').upper().strip() [0]


#caso3
#realização de calculos sem usar o def
opcao = ''
while opcao != 'Sair':
    numero = int(input('Numero: '))
    outro_numero = int(input('Numero: '))

    opcao = input('O que deseja?'
                  '\n1 - Somar'
                  '\n2 - Multiplicar'
                  '\n Sair ----> ')

    if opcao == '1':
        print(f'A soma  é {numero + outro_numero}')
    elif opcao == '2':
        print(f'A multiplicação é {numero * outro_numero}')
    else:
        print('Erro')



#Laços infinitos

a = 0

while True:
    resposta = input('Deseja mais números? [S/N] -> ').upper()[0]
    if resposta == 'N':
        break
    else:
        for i in range(100):
            a += 1
            print(a)


while True:
    print('1. Opção X \n'
          '2. Opção Y \n'
          '3. Sair')
    menu = int(input('Digite a escolha: '))

    if menu == 3:
        break


#tratamento de erros try e except

try:
    numero = int(input('numero: '))
except ValueError:
    print('Apenas numeros')
except:
    print('ERRO: Chamar a TI')

'''

#funções

def bem_vindo():
    print('-*-' * 50)
    print('Bem vindo ao Senai!!!!')
    print('*' * 50)

def mensagem(msg):
    print('*' * 50)
    print(f'{msg}')
    print('*' * 50)

def volume (r):
    return (4/3) * 3.1415 * r ** 3

#uso

#boas vindas
bem_vindo()

#mensagem utilizando uma variavel e retornando ela

nome = 'rafael silva moraes'
mensagem(nome)

#calculo de volume de esfera
volume_esfera = volume(5)
print(volume_esfera)
