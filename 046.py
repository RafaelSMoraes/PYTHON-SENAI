#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar. No final mostre:

#1: Qual é o total gasto na compra
#2: Quantos produtos custam mais de R$1000,00
#3: Qual é o produto mais barato

try:
    soma = 0
    maiores_prod = 0  # Inicializa com 0 para contar a quantidade de produtos
    menor_prod = float('inf')  # Inicializa com um valor muito grande
    quant = 0

    while True:
        nome_prod = input('Nome do produto: ').upper().strip()
        preco_prod = float(input('Preço: '))

        #Definindo a soma dos produtos
        soma += preco_prod #vai retornar na variavel

        #definindo o MAIOR e menor produto:

        #Maior e mais caro produto:
        if preco_prod >= 1000:
            maiores_prod += 1

        #menor e mais barato produto:
        if preco_prod < menor_prod:
            menor_prod = preco_prod

        resposta = input('Deseja continuar? [S/N] --> ').strip().upper()[0]
        if resposta == 'N':
            break

    print(f'O total gasto na compra foi: R$ {soma:.2f}'
          f'\nA quantidade de produtos que custam mais que R$1000 é: {maiores_prod}'
          f'\n O produto mais barato é: R$ {menor_prod}')

except ValueError:
    print('Apenas numeros')