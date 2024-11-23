'''

Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase,
coordenado por uma função

Exemplo:
       ----------------------------
            Senai Show de bola
       ----------------------------
'''

def mensagem(msg):
    tamanho_msg = len(msg)  # Calcula o tamanho da mensagem
    tamanho_linha = tamanho_msg + 6  # Define o tamanho da linha com uma margem de 3 caracteres para cada lado
    print('-' * 50)
    print(f'{msg}')
    print('-' * 50)

frase = input('Digite uma frase: ')

mensagem(frase)