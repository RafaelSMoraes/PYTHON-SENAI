#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
#permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair

try:

    opcao = ''
    deposito = 0
    saque = 0
    saldo_conta = 0

    while opcao != 4:
        opcao = int(input('Seja bem-vindo ao caixa eletronico, selecione uma das opcoes abaixo:'
              '\n 1 - Deposito'
              '\n 2 - Saque'
              '\n 3 - Saldo da conta'
              '\n 4 - Sair'
              '\n---------> '))

        if opcao == 1:
            deposito = float(input('Insira um valor: '))
            saldo_conta += deposito
            print(f'Voce depositou {deposito} reais. Seu novo saldo é: {saldo_conta}')
        elif opcao == 2:
            saque = float(input('Digite um valor a se sacar: '))
            if saque <= saldo_conta:
                saldo_conta -= saque
                print(f'Voce sacou {saque} reais. Seu novo saldo é: {saldo_conta}')
            else:
                print('Saldo insuficiente.')
        elif opcao == 3:
            print(f'Voce possui {saldo_conta} reais')
        elif opcao == 4:
            print('Até breve!')
        else:
            print('Erro!')

except ValueError:
    print('Apenas numeros')

#Criei um MEGAZORD

'''
#correção professor:
try:
    opcao = ''
    saldo = 0
    
    while opcao != 4:
        print('-----------------')
        opcao = int(input('1. Deposito'
                          '\n 2. Saque'
                          '\n 3. Saldo'
                          '\n 4. Sair'
                          '\n ----------------> '))
        if opcao == 1:
            deposito = float(input('Digite a quant a ser depositada: '))
            saldo += deposito
        elif opcao == 2:
            saque = float(input('Digite a quant a ser sacada: '))
            saldo -= saque
        elif opcao == 3:
            print(saldo)
        elif opcao == 4:
            print('Até breve!')
        else:
            print('Opção invalida')
            
except ValueError:
    print('Apenas numeros')
'''