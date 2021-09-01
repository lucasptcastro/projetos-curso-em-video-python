lista = list()
listaimp = list()
listapar = list()
def linha():
    print(' ')

print('-'*10, end='')
print(f'{"Lista de números ímpares e pares":^34}', end='')
print('-'*10)

linha()

add = int(input('Para começar, informe um número: '))
lista.append(add)
if add % 2 == 1:
    listaimp.append(add)
if add % 2 == 0:
    listapar.append(add)

linha()

while True:
    r = int(input('Digite [1] para informar outro número ou [0] para parar: '))
    if r == 1:
        add = int(input('Informe um número: '))
        lista.append(add)
        if add % 2 == 1:
            listaimp.append(add)
        if add % 2 == 0:
            listapar.append(add)
    if r == 0:
        linha()
        print('-'*10, end='')
        print(f'{"Programa Encerrado":^20}', end='')
        print('-'*10)
        linha()
        print(f'➡ Esta é a lista com os números digitados: {lista}')
        print(f'➡ Esta é a lista de números pares: {listapar}')
        print(f'➡ Esta é a lista de números ímpares: {listaimp}')
        break
