cont = 0
par1 = 0
par2 = 0
par3 = 0
par4 = 0
cont2 = 0
for c in range (1):
    a1 = int(input('Informe um valor: '))
    if a1 == 9:
        cont+=1
    if a1 == 3:
        cont2+=1
    if a1 % 2 == 0:
        par1 = a1

    a2 = int(input('Informe um valor: '))
    if a2 == 9:
        cont+=1
    if a2 == 3:
        cont2+=1
    if a2 % 2 == 0:
        par2 = a2

    a3 = int(input('Informe um valor: '))
    if a3 == 9:
        cont+=1
    if a3 == 3:
        cont2+=1
    if a3 % 2 == 0:
        par3 = a3

    a4 = int(input('Informe um valor: '))
    if a4 == 9:
        cont+=1
    if a4 == 3:
        cont2+=1
    if a4 % 2 == 0:
        par4 = a4

t = (a1, a2, a3, a4)
if cont == 0:
    print('O número zero não apareceu nenhuma vez!')
if cont == 1:
    print('O número zero apareceu apenas uma vez!')
if cont > 1:
    print(f'O número zero apareceu {cont} vezes!')
if cont2 == 0:
    print('Não foi digitado nenhum número 3!')
else:
    print(f'O número 3 encontra-se na posição {t.index(3)+1}!')
total = (par1 + par2 + par3 + par4)
if total > 0:
    print('Os números pares foram:',end=' ')
else:
    print('Não foi informado nenhum número par!')
if par1>0:
    print(par1,end=' ')
if par2>0:
    print(par2,end=' ')
if par3>0:
    print(par3,end=' ')
if par4>0:
    print(par4,end=' ')



