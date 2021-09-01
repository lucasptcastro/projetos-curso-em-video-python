exp = str(input('Informe a expressão: '))
pilha = []
cont = 0
cont2 = 0
for simb in exp:
    if simb == '(':
        pilha.append('(')
        cont = cont+1
    if simb == ')':
        pilha.append(')')
        cont2 = cont2 + 1
total = cont + cont2
if total % 2 == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
