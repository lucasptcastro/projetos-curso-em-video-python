exp = str(input('Informe a expressão: '))
x = list(exp).count('(')
y = list(exp).count(')')
if (x+y) % 2 == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')