#Escreva um programa que converta real para o Franco Congolês
#Saída esperada:
#10,00 reais, equivalem a 5052,00 Francos Congoleses

try:
    valor = float(input('Digite um valor em Real Brasileiro:'))
    conversao = 518.30 * valor
    print(f'{valor} reais, equivale a {conversao} Francos Congoleses')

except ValueError:
    print('Apenas numeros')
