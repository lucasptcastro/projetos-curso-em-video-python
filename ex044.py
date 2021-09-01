p = float(input('Informe o valor do produto: '))
print(' ')
print('Tecle [\033[34m1\033[m] para pagamento à vista \033[34mdinheiro\033[m/\033[34mcheque\033[m: \033[33m10% de desconto\033[m')
print('Tecle [\033[34m2\033[m] para pagamento à vista no \033[34cartão\033[m: \033[33m5% de desconto\033[m')
print('Tecle [\033[34m3\033[m] para pagamento em até \033[34m2x no cartão\033[m: \033[33mpreço normal\033[m')
print('Tecle [\033[34m4\033[m] para pagamento \033[34m3x ou mais no cartão\033[m: \033[33m20% de juros\033[m')
print(' ')
r = int(input('Informe aqui: '))

if r == 1:
    v1 = (10*p) / 100
    r1 = p - v1
    print(f'O valor a ser pago será R${r1:.2f}')
elif r == 2:
    v2 = (5*p) / 100
    r2 = p - v2
    print(f'O valor a ser pago será R${r2:.2f}')
elif r == 3:
    print(f'O valor a ser pago será R${p:.2f}')
elif r == 4:
    v3 = (20*p) / 100
    r3 = p + v3
    print(f'O valor a ser pago será R${r3:.2f}')

