lista = ('Bolacha', 1, 'Treloso', 1.50, 'Diamante Negro', 3, 'Macarrão', 2, 'Feijão', 3.50, 'Açúcar', 2.50,'Coca-Cola', 5)
print('-'*40)
print(f'|{"LISTAGEM DE PREÇOS":^38}|')
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'|{lista[pos]:.<30} R$', end='')
    else:
        print(f' {lista[pos]:>3.2f}|')

print('-'*40)