'''
Crie uma função para verificar se um número é par ou ímpar
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

try:

    #utilizacao
    numero = int(input('Digite um numero: '))
    resultado = par_ou_impar(numero)
    print(f'O numero {numero} é {resultado}')

except ValueError:
    print('Inclua apenas números')
