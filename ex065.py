n1 = int(input('Informe um número | Digite 0 para encerrar: '))
cm = 2
m = me = n1
if n1 == 0:
    print('Programa Encerrado!')
else:
    n2 = int(input('Informe um número | Digite 0 para encerrar: '))
    soma = n1 + n2
    if n2 > n1:
        m = n2
    if n2 < n1:
        me = n2
    while n2 != 0:
        n2 = int(input('Informe um número | Digite 0 para encerrar: '))
        soma = soma + n2
        cm = cm + 1
        if n2 > m:
            m = n2
        if n2 < me and n2 != 0:
            me = n2
        if n2 == 0:
            print(f'A média dos valores é {soma/(cm-1)} | O maior número digitado foi {m} e o menor foi {me}')