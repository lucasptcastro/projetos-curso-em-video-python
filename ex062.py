r = int(input('Informe a razão da P.A.: '))
n1 = int(input('Informe o primeiro termpo da P.A.: '))
c = 1
c1 = 1
n = 10
total = 0
print(f'Os dez primeiros termos da P.A. {n1} de razão {r} são: ')
while n != 0:
    total = total + n
    while c <= total:
        print(n1)
        n1 = n1 + r
        c = c + 1
    n = int(input('Quantos termos você quer mostrar a mais: '))
print(' ' '\n--|-- Sistema Encerrado! --|--')

