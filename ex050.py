s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    v = n%2
    if v == 0:
        s = s + n
print(' ')
print(f'A soma dos números pares é: {s}')