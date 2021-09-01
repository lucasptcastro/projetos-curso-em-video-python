c = 0
lista = list()
print('='*10, end='')
print(f'{"Lista de números variados":^30}', end='')
print('='*10)
print(' ')
while c != 'n'.upper():
    add = (input('Informe um número: ')).upper()
    if add in lista:
        print('Número já cadastrado, informe outro.')
    else:
        lista.append(add)
        print('Caso deseje parar de adicionar, digite "N"!')
        print(' ')
    if add == 'N':
        lista.remove('n'.upper())
        lista.sort()
        print(f'Você digitou os seguintes valores: {lista}')
        break