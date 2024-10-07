#descobrir palindromos

palavra = input('Digite uma palavra para saber se ela é ou não um palindromo: ').lower().strip()

if ' ' in palavra:
    palavra = palavra.replace(' ', '') #tira os espaços e pode ser utilizado textos

for palindromo in palavra:
    if palavra == palavra[:: -1]:
        print('é palindromo')
    else:
        print('não é palindromo')

#Legal para se aprofundar mais

soma_idade = 0
quant_mulher_menor_20anos = 0
maior_idade = None
nome_homem_velho = ''

for i in range(4):
    nomes = input('Digite o seu nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()[0] #O zero significa que ele vai interpretar a primera letra

    #soma de idades para media
    soma_idade += idade

    #Soma
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


#Escreva um programa que leia o peso de 7 pessoas,
#e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = None
menor_peso = None
for i in range (7):
    pesos = float(input('Peso: '))

    #reso 1
    if maior_peso == None and menor_peso == None:
        maior_peso = pesos
        menor_peso = pesos

    if pesos > maior_peso:
        maior_peso = pesos

    if pesos < menor_peso:
        menor_peso = pesos

'''   
    #reso 2
    if i == 0
        menor_peso = pesos
        maior_peso = pesos
'''

print(f'O maior peso é {maior_peso}'
      f'\nO menor peso é {menor_peso}')