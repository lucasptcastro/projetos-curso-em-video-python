def fatorial(a, show=False):
    """
    Calcula o fatorial do valor desejado
    O parametro Show, se verdadeiro, ira mostrar o calculo usado para chegar ao resultado do fatorial
    Se falso, ira mostrar apenas o resultado do fatorial
    """
    
    
    #variáveis
    cont = 1
    fat = a
    for c in range(0, a-1): #for de 0 até a-1
        fat = fat * (a - cont)
        cont += 1
    if show == True: #se o paremetro show for True, ele vai mostrar a formatação
        cont = 1
        print(' ')
        print(f'{a} x {a - cont}', end='')
        cont = 2
        for c in range(0, a - cont):
            print(f' x {a-cont}', end='')
            cont += 1
        print(f' = {fat}')
        return f'O fatorial de {a} é {fat}'
    else: #se o parametro show for false, vai mostrar apenas o fatorial
        print(' ')
        return f'O fatorial de {a} é {fat}'

print(fatorial(13, True))

