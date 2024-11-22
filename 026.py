#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela est� entre a faixa ideal, acima ou abaixo do IMC ideal.
try:
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    imc = peso / (altura**2)

    if imc > 25:
        print(f'IMC de {imc} voc� est� sobre o seu peso ideal')
    elif imc > 18.5:
        print(f'IMC de {imc} voc� est� com peso ideal')
    else:
        print(f'IMC de {imc} est� abaixo do ideal')

except ValueError:
    print('Apenas numeros')
