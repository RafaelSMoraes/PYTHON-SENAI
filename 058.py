'''
Crie um programa onde serão informados diversos valores em uma lista.
Caso o número já exista ele não será adicionado.
No final, serão exibidos todos os valores únicos em ordem crescente
'''


'''
def valores_unicos_ordenados_interativo():
  numeros = []
  while True:
    valor = input("Digite um número (ou 'sair' para encerrar): ")
    if valor.lower() == 'sair':
      break
    try:
      numero = int(valor)
      if numero not in numeros:
        numeros.append(numero)
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")

  return sorted(numeros)

# Chamando a função para executar o programa
resultado = valores_unicos_ordenados_interativo()
print("Valores únicos em ordem crescente:", resultado)
'''


#metodo do professor

numeros = []

#estrutura de entrada inderterminada de valores
while True:
  #tratamento de erro
  try:
    #entrada de dados
    x = input('Numero ["sair" para parar]: ')
    if x == 'sair':
      break

    #verificacao de pertencimento
    if int(x) not in numeros:
      numeros.append(int(x))

  except ValueError:
    print('apenas numeros')

#retorno organizado
print(sorted(numeros))
