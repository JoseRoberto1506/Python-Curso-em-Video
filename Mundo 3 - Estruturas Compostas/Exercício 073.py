'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 6 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

teams = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza', 'Fluminense', 'Ceará', 'Internacional', 'América-MG', 'Santos', 'São Paulo', 
         'Atlético-GO', 'Cuiabá', 'Athlético-PR', 'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense')

print("=" * 101)
print(f"Lista de times do Brasileirão {teams}")
print("=" * 101)
print(f"Os 6 primeiros são {teams[:6]}")
print("=" * 101)
print(f"Os 4 últimos são {teams[-4:]}")
print("=" * 101)
print(f"Times em ordem alfabética: {sorted(teams)}")
print("=" * 101)
print(f"A Chapecoense está na {teams.index('Chapecoense') + 1}ª posição.")
