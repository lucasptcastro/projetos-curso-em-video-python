valor = int(input('Informe o valor a ser sacado: '))
total = valor
totalc = 0
ced = 50
while True:
    if total >= ced:
        total = total - ced
        totalc += 1
    else:
        if totalc > 0:
            print(f'Serão sacadas {totalc} de R${ced}')
        totalc = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            break
