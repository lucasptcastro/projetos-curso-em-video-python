n1 = int(input('Informe um número: '))
c = 0
u = 1
p = 1
if (n1 == 1) or (n1 == 2):
    print(1)
else:
    print('1')
    while c < n1:
        t = u + p
        p = u
        u = t
        c = c + 1
        print(p)