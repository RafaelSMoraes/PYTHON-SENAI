#Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar 0000.
#No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag 0000)

'''

#MINHA FORMULA FALHA, NÃO FUNCIONA AHHHAAHHAAHAHAH

quant = 0
soma = 0

while True:
    numero = input('Digite um numero: ')
        if numero.isnumeric():
            quant += 1
            soma += int(numero)
        else:
            resposta = input('Digite 0000 para finalizar -->')
            if resposta == '0000':
                break

print("Quantidade de números:", quant)
print("Soma dos números:", soma)

'''

#Correção professor
try:
    quant = 0
    soma = 0

    while True:
        n = input('Numero: ')
        if n == '0000':
            break

        soma += int(n)
        quant += 1

    print(f'A quantidade de numeros digitados foi: {quant}'
          f'\n A soma dos numeros digitados é: {soma}')

except ValueError:
    print('Apenas numeros')