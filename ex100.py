from random import randint
from time import sleep

def cab(txt):
    print('\033[1;37m-\033[m'*70)
    print(f'|\033[1;37;41m {txt:^67}\033[m|')
    print('\033[1;37m-\033[m'*70)

def espace():
    print(' ')

#variavel
numbers = list()

#FUNÇÃO de sortear números aleatórios
def sorteio(lista):
    
    espace()
    cab('SORTEANDO NÚMEROS')
    print(f'   ▶  Os 5 números sorteados de forma aleatória foram: ',end='')
    
    #sortear numeros de 1 a 10 6 vezes
    for c in range(1,6):
        numbers.append(randint(1,10))
    
    #escrever os números de forma formatada
    for num in numbers:
        sleep(0.4)
        print(f'\033[1;32m{num}\033[m', end=' ', flush=True)
    print('')

#FUNÇÃO de somar os números pares
def somaPar():
    pares = list()
    somaP = 0

    #verificar se o número é par
    for c in range(len(numbers)):
        if numbers[c] % 2 == 0:
            pares.append(numbers[c])
    
    print(f'   ▶  A soma dos números pares informados: ', end='')
    
    #dizer quais foram os números pares listados
    for c in range(len(pares)):
        sleep(0.4)
        print(f'\033[1;32m{pares[c]}\033[m', end=' ', flush=True)

    #dizer qual é a soma dos números pares informados
    for c in range(len(pares)):
        somaP += pares[c]

    print('é igual a', end=' ', flush=True)
    sleep(1.3)
    print(f'\033[1;36m{somaP}\033[m!')
    print('')


sorteio(numbers)
somaPar()
