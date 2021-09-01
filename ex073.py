brasileirao = ('Atlético-MG','Internacional','São Paulo','Flamengo','Palmeiras','Santos','Grêmio','Fluminense','Bahia',
               'Athetico-PR','Sport','Corinthians','Fortaleza','Ceará','Atlético-GO','Bragantino','Vasco','Coritiba','Botafogo','Goiás')
print(f'Os 5 primeiros colocados são: {brasileirao[:5]}')
print('--|--')
print(f'Os 4 últimos colocados são: {brasileirao[-4:]}')
print('--|--')
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}')
print(f'O Flamengo está na posição: {brasileirao.index("São Paulo")+1}')
