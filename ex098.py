from time import sleep

def espace():
    print(' ')

def line():
    print('='*45)

def contador():
    espace()
    line()
    
    #contagem de 1 a 10
    print(f'⏩ Contagem de 1 até 10, pulando de 1 em 1:')
    print('    ▶', end='  ', flush=True)
    sleep(0.3)
    for c in range (0,10):
        print(f'{c+1}', end=' ', flush=True)
        sleep(0.3)
    print('')
    line()
    
    #contagem de 10 a 0, de 2 em 2
    print(f'⏩ Contagem de 10 até 0, pulando de 2 em 2:')
    print('    ▶', end='  ', flush=True)
    sleep(0.3)
    for c in range (10, -1, -2):
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
    print('')
    line()    
    
    #contagem personalizada
    print('⏩ Sua vez de personalizar!')
    start = int(input('    ▶ Informe o início: '))
    end = int(input('    ▶ Informe o final: '))
    step = str(input('    ▶ Informe os passos: '))
    print('    ▶', end='  ')

    #condição para caso o 'step' recebe nada
    if step == '':
        if end > 0: #caso o end seja positivo
            for c in range(start, end+1, 1):
                print(f'{c}', end=' ', flush=True)
                sleep(0.3)
        else: #caso o end seja negativo
            for c in range(start, end-1, -1):
                print(f'{c}', end=' ', flush=True)
                sleep(0.3)
        print('')
        line()
    
    #condição para caso seja uma ordem decrescente
    elif end < start:
        if '-' in step: #caso os passos estejam em negativo
            for c in range(start, end-1, int(step)):
                print(f'{c}', end=' ', flush=True)
                sleep(0.3)
        else: #caso os passos estejam em positivo
            for c in range(start, end-1, -int(step)):
                print(f'{c}', end=' ', flush=True)
                sleep(0.3)

    #condição para caso seja uma ordem normal
    elif step != None:
        for c in range(start, end+1, int(step)):
            print(f'{c}', end=' ', flush=True)
            sleep(0.3)
    print('')
    line()
    espace()

contador()