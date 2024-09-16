#Crie um programa que verifica se
#uma pessoa pode ser doadora de sangue,
#considerando a idade e os critérios de saúde.

'''

#meu metodo:

idade = int(input('Insira a sua idade para saber se voce esta apto ou não para doar sangue: '))

if idade >= 16:
    print('Você atende a idade minima para doar sangue, por favor prossiga')
else:
    print('Você nao possui a idade minima para doar sangue, tente outro ano')
    exit()

doacao_sangue = input('Você já doou sangue esse ano? [s/n] ').lower().strip()[0]

if doacao_sangue == 's':
    print('Doe o seu sangue novamente no ano que vem')
    exit()
else:
    print('Ok você pode doar sangue')

peso = float(input('Insira o seu peso: '))

if peso >= 50:
    print('Seu peso está ok, prossiga')
elif peso >= 47.5:
    print('Você pode doar sangue, mas precisa comer um pouco mais. Prossiga ')
else:
    print('Voce está abaixo do peso, por favor vá ao nutricionista')
    exit()

alimento = input('Você comeu algum alimento gorduroso? [s/n] ').lower().strip()[0]

if alimento == 's':
    print('Tente novamente em outro dia')
    exit()
else:
    print('Ok, você está apto')

sono = float(input('Insira a sua quantidade de horas de sono: '))

if sono >= 6:
    print('Você tem a quantidade de horas minimas para doar sangue.')
else:
    print('Você precisa dormir mais')
    exit()

criterio = input(f'Você possui {idade} anos, pesa {peso}kg e '
                 f'teve mais de {sono} horas de sono está apto para doar sangue')

'''

#metodo do professor, o 'escudo', começa da positiva (if) para a negativa (else)
#lembra a formação de um site

idade = int(input('idade: '))
if idade >= 16 and idade < 69:
    peso = float(input('Peso: '))
    if peso > 50:
        sono = int(input('Horas de sono: '))
        if sono > 8:
            doacao_sangue = input('Você doou sangue? [S/N] ').upper().strip()[0]
            if doacao_sangue == 'S':
                print('Você pode doar')
            else:
                print('Você já doou sangue, tente novamente ano que vem')
        else:
            print('Precisa dormir mais')
    else:
        print('Peso incorreto')
else:
    print('idade incorreta')