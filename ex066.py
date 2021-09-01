n1 = int(input('Informe um número, use (999) para parar: '))
soma = n1
cont = 1
while True:
    n1 = int(input('Informe um número, use (999) para parar: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')