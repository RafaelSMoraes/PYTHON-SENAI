'''
Crie um programa que pede ao usuário para digitar dois números e
em seguida, divida o primeiro número pelo segundo número.
No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
como uma string ou o número zero.

ZeroDivisionError ; ValueError

'''

try:
    while True:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))

        divide_n1_n2 = n1 / n2

        print(f'A divisão dos numeros {n1} e {n2} é: {divide_n1_n2}')

except ZeroDivisionError:
    print('numero nao divisivel por 0 (zero)')
except ValueError:
    print('Apenas numeros')