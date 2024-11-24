# Faça um programa com uma função maior e menor,
# que leia uma lista com 5 valores informados pelo usuário
# e retorne esses valores e a posição deles
def maior_e_menor(lista):
    maior = lista[0]
    menor = lista[0]
    pos_maior = 0
    pos_menor = 0

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            pos_maior = i
        elif lista[i] < menor:
            menor = lista[i]
            pos_menor = i

    return maior, pos_maior, menor, pos_menor

# Entrada do usuário
lista = []
for i in range(5):
    num = float(input("Digite um número: "))
    lista.append(num)

# Chamando a função e imprimindo os resultados
resultado = maior_e_menor(lista)
print("O maior valor é:", resultado[0], "na posição", resultado[1])
print("O menor valor é:", resultado[2], "na posição", resultado[3])