#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
#Saida esperada: O salário de 6000 com o reajuste de 60% será de : 9600

try:
    salario = float(input('Insira o Salario: '))
    reajuste = salario * 0.60
    valor_final = salario + reajuste

    print(f'O salario de {salario} com o reajuste de 60% será de: {valor_final}')

except ValueError:
    print('Apenas numeros')
