# esse eu fiz com ajuda do video
numeros = list()
cont = 0
def linha():
    print(' ')

print('='*10, end='')
print(' CADASTRO NUMÉRICO ', end='')
print('='*10)

linha()

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
print(f'Os valores de forma crescente, são: {numeros}')




