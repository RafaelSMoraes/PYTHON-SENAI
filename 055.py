'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois, deve mostrar para cada palavra, suas vogais



#meu metodo

palavras = ("PYTHON", "PROGRAMACAO", "TUPLA", "EXERCICIO", "LINGUAGEM")

for palavra in palavras:
    try:
        vogais = ""
        for letra in palavra:
            if letra in "AEIOU":
                vogais += letra
        print(f"Palavra: {palavra}, Vogais: {vogais}")
    except TypeError:
        print(f"A palavra '{palavra}' não é uma string válida.")

'''


#metodo professor

palavras = ("PYTHON", "PROGRAMACAO", "TUPLA", "EXERCICIO", "LINGUAGEM")

for palavra in palavras:
    print(palavra, end=' - ')

    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(letra, end=', ')
    print()