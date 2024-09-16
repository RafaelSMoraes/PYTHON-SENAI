#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
#raiz quadrada.
#Saída esperada:
#A dobro de 9 é : 18
#A triplo de 9 é : 27
#A raiz quadrada de 9 é : 3

#Entrada de dados
n1 = float(input('Digite um numero para ser mostrado o seu Dobro, Triplo e Raiz Quadrada: '))

#calculos
dobro = n1 * 2
Triplo = n1 * 3

#Calculo de raiz quadrada
raiz = n1**0.5 #Ou numero ** (1/2)

#saida de dados
print(f'O dobro de {n1} é:{dobro} \n O triplo de {n1} é: {Triplo} \n E a raiz de {n1} é {raiz:.2f}')