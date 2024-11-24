'''

Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”

'''

filmes = (
    "Avatar",
    "Vingadores: Ultimato",
    "Titanic",
    "Star Wars: O Despertar da Força",
    "Jurassic World",
    "Os Vingadores",
    "Furiosos 7",
    "Frozen II",
    "O Rei Leão",
    "Harry Potter"
)

# 1. Apenas os 3 primeiros mais assistidos
primeiros_tres = filmes[:3]

# 2. Os últimos 2 mais assistidos
ultimos_dois = filmes[-2:]

# 3. A lista em ordem alfabética
filmes_ordenados = sorted(filmes)

# 4. Em que posição está “O Rei Leão”
posicao_rei_leao = filmes.index("O Rei Leão") + 1  # +1 para ajustar à contagem humana

# Exibindo os resultados
print("Os 3 primeiros filmes mais assistidos:", primeiros_tres)
print("Os últimos 2 filmes mais assistidos:", ultimos_dois)
print("Lista de filmes em ordem alfabética:", filmes_ordenados)
print("A posição de 'O Rei Leão' é:", posicao_rei_leao)
