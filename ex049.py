n = int(input('Informe o número referente a tabuada que deseja ver: '))
print(' ')
print('   \033[31;40m=-= TABUADA =-=\033[m')
v1 = n+10
a = n
b = 0
for c in range(n,v1):
    b = b + 1
    a = a + 1
    c = n * b
    print(f'{n} + {b} = {a} ' '|' f' {n} * {b} = {c}')