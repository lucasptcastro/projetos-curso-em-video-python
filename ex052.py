n1 = int(input('Informe um número inteiro para saber se é primo: '))
t = 0
t2 = 0
for c in range(1,n1+1):
    if n1 % c == 0:
        t += 1
    else:
        t2 += 1
print(f'\n\033[mO número {n1} foi dividido {t} vezes')
if t == 2:
    print(f'O número \033[34m{n1}\033[m é primo!')
else:
    print(f'O número \033[31m{n1}\033[m não é primo!')