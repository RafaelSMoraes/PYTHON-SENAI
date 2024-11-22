#Faça um programa que leia um número e retorne o fatorial !

#4! = 4 x 3 x 2 x 1

'''
n1 = int(input('Digite o número que deseja encontrar o fatorial: '))
multiplicação = n1

while n1 != 1:
     n1 = n1 - 1
     multiplicação *= n1


     print(multiplicação)

'''

#CORREÇÃO
try:
     n = int(input('Numero: '))
     fat = 1

     '''
     while n != 1:
          fat = fat * n
          n = n - 1
          print(n, fat)
     '''

     c = 1
     while c != n:
          c = c + 1
          fat = fat * c

     print(fat)

except ValueError:
    print('Apenas numeros')