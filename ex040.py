n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
m = (n1 + n2) / 2

if m < 5:
    print('\033[31mVocê foi REPROVADO!')
elif m >= 5 and m <= 6.99:
    print('\033[33mVocê está de RECUPERAÇÃO!')
elif m >= 7:
    print('\033[32mParabéns! Você está APROVADO!')