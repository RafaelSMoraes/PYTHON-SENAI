#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2)

if imc > 25:
    print(f'IMC de {imc} você está sobre o seu peso ideal')
elif imc > 18.5:
    print(f'IMC de {imc} você está com peso ideal')
else:
    print(f'IMC de {imc} está abaixo do ideal')
