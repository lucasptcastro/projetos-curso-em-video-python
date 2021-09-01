n1 = int(input('Informe um número para realizar uma operação escolhida: '))
n2 = int(input('Informe outro número: '))

print(' ')

print('[1] Soma')
print('[2] Multiplicação')
print('[3] Maior')
print('[4] Novos Números')
print('[5] Sair do programa')

print(' ')

r = int(input('Agora escolha a operação que deseja realizar: '))

while r != 5:
    if r == 1:
        s = n1 + n2
        print(' ')
        print(f'A soma entre {n1} e {n2} é {s}')
    if r == 2:
        m = n1 * n2
        print(' ')
        print(f'A multiplicação entre {n1} e {n2} é {m}')
    if r == 3:
        if n1 > n2:
            print(' ')
            print(f'O maior número entre {n1} e {n2} é {n1}')
        if n2 > n1:
            print(' ')
            print(f'O maior número entre {n1} e {n2} é {n2}')
    if r == 4:
        print(' ')
        n1 = int(input('Escolha um novo número: '))
        n2 = int(input('Escolha um novo segundo número: '))
    print(' ')
    print('[1] Soma')
    print('[2] Multiplicação')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do programa')
    print(' ')
    r = int(input('Escolha novamente: '))
if r == 5:
    print(' ')
    print('O programa está encerrado!')
