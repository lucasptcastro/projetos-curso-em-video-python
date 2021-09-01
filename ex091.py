from random import randint
from time import sleep
from operator import itemgetter

dado = {'Jogador1':randint(1,6), 'Jogador2':randint(1,6), 'Jogador3':randint(1,6), 'Jogador4':randint(1,6)}
rank = list()

for k, v in dado.items():
    print(f'O \033[1:34m{k}\033[m tirou \033[1:32m{v}\033[m no dado!')

rank = sorted(dado.items(), key=itemgetter(1), reverse=True)

print(' ')
for p, v in enumerate(rank):
    print(f'Em \033[1:33m{p+1}º\033[m lugar ficou o \033[1:34m{v[0]}\033[m que tirou \033[1:32m{v[1]}\033[m nos dados!')
    sleep(1.1)


