from time import sleep

def cab(txt):
    print('\033[1;32m-\033[m'*45)
    print(f'\033[1;32m| {txt:^42}|\033[m')
    print('\033[1;32m-\033[m'*45)

def espace():
    print(' ')

def maior(* valores):
    #variaveis
    m = 0
    numeros = len(valores)
    
    cab('NÚMEROS MAIORES')
    sleep(1.5)
    print('   ▶ Analisando...')
    sleep(0.9)

    #condição para caso seja informado apenas 1 valor ou mais
    if len(valores) == 1:
        print(f'   ▶ Ao todo, foi informado apenas {numeros} número:', end=' ', flush=True)
    #condição para caso nenhum número seja informado
    elif len(valores) == 0:
        print(f'   ▶ Nenhum número foi informado!', end='', flush=True)
    #condição para caso seja informado mais de 1 numero
    else:
        print(f'   ▶ Ao todo, foram informados {numeros} números:', end=' ', flush=True)
        
    #para cada numero em valores, informe o número
    for num in valores:
        sleep(0.3)
        print(num, end=' ', flush=True)

    #para cada numero em valores, informe somente o maior número
    for num in valores:
        if num > m:
            m = num
    
    print('')
    sleep(0.9)
    print(f'   ▶ O maior número informado foi {m}')

maior(3, 4, 1, 15, 7, 23, 41, 11, 29)
maior(4, 8, 1, 9, 12, 28)
maior(4, 1, 2)
maior(4, 9)
maior(7)
maior()

espace()