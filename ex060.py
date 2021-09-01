#from math import factorial
#n1 = int(input('Digite um número para calcular seu fatorial: '))
#f = factorial(n1)
#print(f'O fatorial de {n1} é {f}!')

#ou

n1 = int(input('Informe um número para saber o seu fatorial: '))
c = n1
f = 1
print(f'{n1}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c-1
print(f'{f}')

