'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:
    A média de idade do grupo
    Qual é o homem mais velho
    Quantas mulheres têm menos de 20 anos
'''

soma_idade = 0
quant_mulher_menor_20anos = 0
maior_idade = None
nome_homem_velho = ''

for i in range(4):
    nomes = input('Digite o seu nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()[0] #O zero significa que ele vai interpretar a primera letra

    #soma de idades
    soma_idade += idade

    if sexo == 'M' and maior_idade == None:
        maior_idade = idade
    elif sexo == 'M' and idade > maior_idade:
        nome_homem_velho = nomes
        maior_idade = idade

    if sexo == 'F' and idade < 20:
        quant_mulher_menor_20anos += 1

print(f'A média de idades do grupo é {soma_idade / 4}')
print(f'O {nome_homem_velho} é o homem mais velho e tem: {maior_idade}')
print(f'Quantidade de mulheres que tem menos de 20 anos: {quant_mulher_menor_20anos}')