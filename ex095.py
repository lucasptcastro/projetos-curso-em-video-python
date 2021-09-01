#variaveis
players = dict()
goals = list()
allP = list()
cont = 0
Tgoals = 0
id = 0


def espace():
    print(' ')


while True:
    #menu
    espace()
    print('='*50)
    print(f'|\033[1:31:40m{"COLETA DE DADOS":^48}\033[m|')
    print('='*50)
    espace()
    #jogadores
    players['name'] = str(input('➡ Informe o nome do jogador: ')).title()
    players['matches'] = int(input(f'➡ Informe quantas partidas {players["name"]} jogou: '))
    for c in range(0, players['matches']):
        goals.append(int(input(f'➡ Informe a quantidade de gols marcados na {cont+1}ª partida: ')))
        Tgoals = Tgoals + goals[cont]
        cont += 1
    #adicionarNaLista
    cont = 0
    players['goals'] = goals[:]
    goals.clear()
    players['Tgoals'] = Tgoals
    Tgoals = 0
    allP.append(players.copy())
    question = str(input(f'{"▶":>5} Informe "C" para adicionar outro jogador ou "P" para parar: ')).upper()
    if question == "C":
        continue
    else:
        break


espace()
print('='*50)
print(f'|\033[1:31:40m{"RESULTADO":^48}\033[m|')
print('='*50)
print(f'{"ID"} {"NAME":<15} {"GOALS"} {"TOTAL":>20}')
print('='*50)
espace()


#resultado
for c in range(len(allP)):
    print(f'{id} {allP[id]["name"]:<15} {allP[id]["goals"]} {allP[id]["Tgoals"]:>40} {"":>41}')
    id += 1
espace()


#mostrarDados
while True:
    cont = 0
    question2 = int(input('Informe o ID do jogador para ver o levantamento de gols: '))
    for c in range(len(allP[question2]['goals'])):
        print(f'No {cont+1}ª jogo, marcou: {allP[question2]["goals"][cont]} gols!')
        cont += 1
    if question2 == 999:
        break