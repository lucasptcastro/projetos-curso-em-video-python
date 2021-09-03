#print(' ')
#def ficha():
    #nome = str(input(f'▶ Informe o nome do jogador: ')).title().strip()
    #g = input(f'▶ Informe quantos gols ele fez: ').strip()
    #if nome == '' and g == '':
        #return f'     ▶ O jogador \033[1;32mdesconhecido\033[m fez \033[1;36m0\033[m gols!'
    #elif nome == '':
        #return f'     ▶ O jogador \033[1;32mdesconhecido\033[m fez \033[1;36m{g}\033[m gols!'
    #elif g == '':
        #return f'     ▶ O jogador \033[1;32m{nome}\033[m fez \033[1;36m0\033[m gols!'
    #else:
        #return f'     ▶ O jogador \033[1;32m{nome}\033[m fez \033[1;36m{g}\033[m gols!'

#print(ficha())

#ou

def ficha(name="Desconhecido", goals=0):
    return print(f'O jogador {name} marcou {goals} gols!')

n = str(input('Informe o nome do jogador: ')).title()
g = str(input('Informe quantos gols o jogador marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == ''.strip():
    ficha(goals=g)
else:
    ficha(n, g)

