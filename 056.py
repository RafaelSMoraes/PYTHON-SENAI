'''
Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
'''


numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze"
)

#meu metodo

try:
    numero = int(input("Digite um número de 0 a 15: "))

    if 0 <= numero <= 15:
        print(f"O número {numero} por extenso é: {numeros_extenso[numero]}")
    else:
        print("Número inválido. Digite um número entre 0 e 15.")


except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
except IndexError:
    print('Somente 0 a 15')


#metodo professor

try:
    numero = int(input('Numero de 0 a 15: '))
    print(numeros_extenso[numero]) #fatiamento, coloque 0 e retorna Zero

except ValueError:
    print('Apenas numeros')
except IndexError:
    print('Somente numeros entre 0 a 15')