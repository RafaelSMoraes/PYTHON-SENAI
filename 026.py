#Crie um programa para analisar o IMC de uma pessoa,
# e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = (altura / peso**2)

if imc < 16:
    print('Baixo')