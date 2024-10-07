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