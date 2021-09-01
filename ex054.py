from datetime import date
a = 0
c = 0
c2 = 0
ano = date.today().year
for c in range(1,8):
    a += 1
    n = int(input(f'Informe o ano de nascimento da pessoa {a}: '))
    a1 = ano - n
    if a1 >= 21:
        c += 1
    else:
        c2 += 1
print(f'{c} pessoas já são de maior!')
print(f'{c2} pessoas não são de maior!')
