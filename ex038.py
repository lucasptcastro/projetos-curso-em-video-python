n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print(f'O número {n1} é maior que {n2}!')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}!')
else:
    print('Ambos os números são iguais!')