#Escreva um programa que:
#calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

#meu metodo
soma = 0

for numero in range (0, 501):
    if numero % 4 == 0:
        soma += numero
print(f'A soma dos multiplos de 4 é: {soma}')

#metodo professor

'''
a minha forma foi a mesma dele, cabuloso isso ai

for i in range(0, 501, 4):#vai somar de 4 em 4
    print(i)

'''