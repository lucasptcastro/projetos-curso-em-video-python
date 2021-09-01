s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(f'Há {cont} números que são ímpares e múltiplos de 3 entre 1 e 500.' f'\nA soma entre eles são: {s}')

