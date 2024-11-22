#Escreva um programa que leia 10 números,
# se for ímpar deve ser descartado,
# se não, deve ser agregado a uma soma
try:
    soma = 0
    for i in range(0, 11):
        numero = int(input('Digite um numero: '))
        if numero % 2 == 0:
            soma += numero
    print(f'A soma é {soma}')

except ValueError:
    print('Apenas numeros')

#Foi realizada a revisão do professor e precisava apenas de uma variavel
#Foi criada a variavel 'numero' para ser realizado a soma
