p = float(input('Informe o seu peso: '))
a = float(input('Informe a sua altura: '))

imc = p / (a*a) * 10000
r = round(imc, 1)

if r < 18.5:
    print('Seu status é ABAIXO DO PESO!')
elif r >= 18.5 and r < 25:
    print('Seu status é PESO IDEAL!')
elif r >= 25 and r < 30:
    print('Seu status é SOBREPESO!')
elif r >= 30 and r < 40:
    print('Seu status é OBESIDADE!')
elif r > 40:
    print('Seu status é OBESIDADE MÓRBIDA!')

