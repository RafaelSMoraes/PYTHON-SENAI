#Escreva um programa que verifique se uma palavra é um palíndromo.

'''

palavra = input('Digite uma palavra para saber se ela é ou não um palindromo: ').lower().strip()

if ' ' in palavra:
    palavra = palavra.replace(' ', '')

for palindromo in palavra:
    if palavra == palavra[:: -1]:
        print('é palindromo')
    else:
        print('não é palindromo')

'''

#metodo professor

palavra1 = input('Palavra: ').strip().strip()

if ' ' in palavra1:
    palavra1 = palavra1.replace(' ', '')

comp = 0

for i in range(0, len(palavra1)):
    if palavra1[i] == palavra1[-1-i]:
        comp += 1

if comp == len(palavra1):
    print('é palindromo')
else:
    print('não é palindromo')

'''
#segundo metodo do professor

palavra2 = input('palavra: ')

if ' ' in palavra2:
    palavra2 = palavra2.replace(' ', '')
    
if palavra2 == palavra2[::-1]:
    print('é palindromo')
else:
    print('não é palindromo')

'''
