#Escreva um programa que leia o raio de uma esfera, e calcule
# o seu volume e área.
#V = (4/3) . π . r³
#A = 4 . π . r²

#leitura de dados
raio = float(input('digite o raio:'))

#calculo de volume e area
volume = (4 / 3) * 3.14 * (raio**3)
area = 4* 3.14 * (raio**2)

#saida de dados
print(f'o volume da esfera é: {volume: .2f}, e a área é de {area: .2f}')