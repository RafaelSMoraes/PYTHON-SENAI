#Escreva um programa que imprima todos os números pares entre dois números
# fornecidos pelo usuário.

'''
#minha formula

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))

for i in range (n1, n2 +1):
    if(i %2 == 0):
        print(i,'Numeros pares')

for ele in range (n2, n1)[:: -1]:
    if(ele %2 == 0):
        print(ele, 'numeros pares')

'''
#metodo professor
try:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))

    if inicio < fim:
        for i in range(inicio, fim):
            if i % 2 == 0:
                print(i)
    else:
        for i in range(inicio, fim -1):
            if i % 2 == 0:
                print(i)
except ValueError:
    print('Apenas numeros')
