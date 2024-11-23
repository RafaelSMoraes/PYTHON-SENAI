#Crie um programa que tenha a função área(),
#que receba as dimensões de um muro retangular e mostra a área do terreno

try:
    def area():
        largura = float(input('Digite a largura'))
        comprimento = float(input('Digite o comprimento'))

        area = largura * comprimento

        print(f'A área do terreno é {area:2.f} m²')

    #chamada da função
    area()

except ValueError:
    print('Inclua apenas números')


