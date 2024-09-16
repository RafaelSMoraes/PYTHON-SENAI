#Escreva um programa que leia um tipo de dado e usando a função type(),
# etorne ao usuário, qual o tipo de dado informado

 dado = input('digite algo: ')

#a função type irá determinar se o que foi colocado é uma string ou numero
#O retorno pode ser "<class 'str'>
 print(type(dado))

# print(type(1)), retorna como 'int'
# print(type(1.5)) retorna como 'float'
#print(type('a')) retorna como 'str'