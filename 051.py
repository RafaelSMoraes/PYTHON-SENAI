'''
Crie uma função para verificar se um número é par ou ímpar
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par' #usando o return para ficar mais "elegante" haha
    else:
        return 'impar'


#utilização

numero = int(input('Digite um numero: '))
resultado = par_ou_impar(numero)
print(f'f O numero {numero} é {resultado}')