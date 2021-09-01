r = int(input('Informe a razão da \033[31mP.A\033[m: '))
a1 = int(input('Informe o primeiro termo da \033[31mP.A\033[m: '))
v = r*10
print(' ')
print('Os 10 primeiros termos dessa \033[31mPROGRESSÃO ARITMÉTICA\033[m são:')
for c in range(a1,v,r):
    print(c)
