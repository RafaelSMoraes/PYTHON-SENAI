#Crie um programa que leia um nome, e mostre o primeiro e o último nome
'''
Saída esperada:
Luis Felipe Tatin Vlatkovic
Primeiro nome: Luis
Último nome: Vlatkovic
'''

#Leitura da variavel  nome, atentando para remoção de espaços antes e depois
nome = input('Digite o seu nome: ').strip()

primeiro_nome = nome.find(' ')
letras_1nome = nome[0:primeiro_nome]

#retorno das informações, fatiando a partir da leitura da posição de espaços
print(f'Primeiro Nome: {letras_1nome}')
print(f'Ultimo Nome: {nome[nome.rfind(' ') +1:]}') #metodo para pegar o ultimo nome