matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = []
contador = 0
maior = 0


def espaco ():
    print(' ')

def linhas ():
    print('-'*50)

espaco()
linhas()
espaco()

for c in range(0,3):
    for p in range(0,3):
        matriz[c][p] = int(input(f'Informe um número para a posição [{c}, {p}]: '))

espaco()
linhas()
espaco()

for c in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[p][c]:^5}]', end='')
    print()

for c in range(0,3):
    for p in range(0,3):
        if matriz[c][p] % 2 == 0:
            somaP = matriz[c][p] + contador
            contador = somaP

for c in range(0,3):
        if matriz[c][1] > maior:
            maior = matriz[c][1]

espaco()
linhas()
espaco()

print(f'A soma dos valores pares da matriz é igual a \033[1:32m{somaP}\033[m!')
print(f'A soma dos valores da terceira coluna é igual a \033[1:32m{matriz[2][0] + matriz[2][1] + matriz[2][2]}\033[m!')
print(f'O maior valor asegunda linha é igual a \033[1:32m{maior}\033[m!')