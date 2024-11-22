#Escreva um programa que leia um número n inteiro qualquer
# e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

try:
    n = int(input('n: '))

    atual = 1
    ant = 0
    aux = 1
    while aux <= n:
        if aux == 1:
            print(0)
        elif aux == 2:
            print(1)
        else:
            prox = atual + ant
            print(prox)
            ant = atual
            atual = prox

        aux += 1
except ValueError:
    print('É aceito apenas numeros')