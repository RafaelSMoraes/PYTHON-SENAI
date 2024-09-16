'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

frase = input(f'Copie e cole a sua frase: ').strip().lower() #o .lower irá ler a frase
#em minuscula para nao dar erro

letra_aparicao = frase.count('a')

#esse replace ira trocar os 'a' com acento para o normal
frase = frase.replace('ã', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('á', 'a')
frase = frase.replace('â', 'a')

print(f'A quantidadde de letras "a" na frase é?: {letra_aparicao}' #Quantas vezes aparece
      f'\n Primeiro a: {frase.find('a') + 1}' #numero que aparece o Primeiro a, o +1 transforma o 0 por 1
      f'\n Ultimo a: {frase.rfind('a') + 1}') #numero que aparece o ultimo a

