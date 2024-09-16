# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite o seu nome: ').strip()

quant_total = len(nome) #ira contar quantas letras tem o nome
quant_espacos = nome.count(' ') #vai contar quantos espaços tem
quant_sem_espacos = quant_total - quant_espacos #ira fazer a subtração de espaços

#letras primeiro nome
primeiro_espaco = nome.find(' ')
letras_1_nome = len(nome[0:primeiro_espaco])

print(nome.upper())
print(nome.lower())

print(f'{quant_sem_espacos}') #quantas letras tem ao todo sem considerear os espaços

print(f'Sem espaços V2 {len(nome.replace(' ', ''))}') #ira trocar os espacos pelo "nada"

print(nome.find(' ')) # Quantas letras tem o primeiro nome

print(f'Letras 1 nome v2 {letras_1_nome}')