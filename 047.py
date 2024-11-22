'''

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1


# metodo inacabado

#opcao = ''
#saque = 0
#saldo_conta = 0

while True:
    while opcao != 3:
        opcao_1 = int(input('Seja bem-vindo ao caixa eletronico, selecione uma das opcoes abaixo:'
                           '\n 2 - Saldo da conta'
                           '\n 3 - Sair'
                           '\n---------> '))

        opcao_2 = int(input('As seguintes celulas estão disponiveis para sacar:'
                        '\n 2. R$ 20'
                           '\n 4. R$ 1'))
        if opcao_2 == 1:
            if saque <= saldo_conta:
                saldo_conta -= saque
                print(f'Voce sacou {saque} reais. Seu novo saldo é: {saldo_conta}')
            else:
                print('saldo insuficiente')
                break

'''
try:
      #metodo professor
      valor_saque = int(input('Digite a quantidade a ser sacada: '))

      cedulas_50 = valor_saque // 50
      valor_saque = valor_saque % 50

      cedulas_20 = valor_saque // 20
      valor_saque = valor_saque % 20

      cedulas_10 = valor_saque // 10
      valor_saque = valor_saque % 10

      cedulas_1 = valor_saque

      print(f'Quantidade de notas de 50: {cedulas_50}'
            f'\n Quantidade de notas de 20: {cedulas_20}'
            f'\n Quantidade de notas de 10: {cedulas_10}'
            f'\n Quantidade de notas de 1: {cedulas_1}')
except ValueError:
      print('Apenas numeros')