import random
from time import sleep
palpites = list()
palpites2 = list()
contador = 0

def espaco ():
    print(' ')

espaco()
print('=-='*17)
print(f'| \033[1:30:46m{"MEGASENA":^47}\033[m |')
print('=-='*17)
espaco()

#pergunta sobre os palpites
pergunta = int(input('⏩ Informe a quantidade de palpites a serem gerados: '))
espaco()

for c in range(0, pergunta):
    for p in range(0,6):
        nAleatorio = random.randint(1,60)
        if nAleatorio not in palpites2:
            palpites2.append(nAleatorio)
    if len(palpites2) < 6:
        nAleatorio = random.randint(1, 60)
        if nAleatorio not in palpites2:
            palpites2.append(nAleatorio)
    palpites.append(palpites2[:])
    print(f'➡ Tabela número {contador + 1}: ', end='')
    print(f'{palpites[c]}')
    contador += 1
    palpites2.clear()
    sleep(1)



