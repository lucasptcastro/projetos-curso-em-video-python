n1 = int(input('Informe um número ou use (999) para parar: '))
n = t = 0
cn = 2
if n1 == 999:
    print('Programa Encerrado! Não teve nenhuma soma, nem número digitado!')
else:
    n2 = int(input('Informe um número ou use (999) para parar: '))
    soma = n1 + n2
    if n2 == 999:
        print(f'Programa Encerrado! Não teve nenhuma soma! O número inserido foi {n1}')
    else:
        while n2 != 999:
            n2 = int(input('Informe um número ou use (999) para parar: '))
            soma = soma + n2
            cn = cn + 1
            if n2 == 999:
                print(f'Programa Encerrado!A soma dos números digitados é {soma - 999}! Foram digitados {cn-1} números!')