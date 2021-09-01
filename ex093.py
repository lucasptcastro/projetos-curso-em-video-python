from time import sleep
players = dict()
goals = list()
cont = 1
calcG = 0
def espace():
    print(' ')

espace()
print('='*50)
print(f'|\033[1;32m{"COLETA DE DADOS":^48}\033[m|')
print('='*50)
espace()

#dados do jogador
players['name'] = str(input('⏩ Informe o nome do jogador: ')).title()


espace()
print('='*50)
print(f'| \033[1;32;40m{"MARCAÇÃO DE GOLS":^48}\033[m|')
print('='*50)
espace()

#quantidade de gols por partida
players['matches'] = int(input('⏩ Informe quantas partidas jogou: '))
for c in range(0, players['matches']):
    goals.append(int(input(f'⏩ Informe quantos gols você fez na {cont}ª partida: ')))
    cont += 1
    calcG = calcG + goals[c]
players['goalsT'] = calcG

espace()
print('='*50)
print(f'|\033[1;32;40m{"INFORMAÇÕES DO JOGADOR":^48}\033[m|')
print('='*50)
espace()

#resultados
print(f'▶ O nome do jogador é {players["name"]}!')
print(f'▶ {players["name"]} jogou {players["matches"]} partidas!')

#gols
cont = 0
sleep(1)
for c in enumerate(goals):
    print(f'{"▶":>5} Na {cont+1}ª partida, marcou {goals[cont]} gols!')
    cont += 1
    sleep(2)
print(f'▶ Obtendo um total de {players["goalsT"]} gols!')

