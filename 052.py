#Crie uma tupla com 5 nomes de países e exiba os países em ordem alfabética.

paises = ("Brasil", "Argentina", "Estados Unidos", "Japão", "China")

# Ordena a tupla em ordem alfabética
paises_ordenados = sorted(paises)

# Exibe os países em ordem alfabética
print("Países em ordem alfabética:")
for pais in paises_ordenados:
  print(pais)
