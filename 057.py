'''
Escreva um programa que crie uma lista com os números de 1 a 10 e,
em seguida, exiba apenas os números ímpares da lista.
'''

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#numeros impares em UMA unica lista

lista_2 = [x for x in range(1,11) if x % 2 != 0]
print(f'Numeros impares: {lista_2}')


# Imprimimos os números ímpares
# meu metodo:

'''
print("Números ímpares:")
for numero in numeros:
    if numero % 2 != 0: #usando igual igual '==' dá, mas diferente de '!=' tambem funciona
        print(numero)
'''
