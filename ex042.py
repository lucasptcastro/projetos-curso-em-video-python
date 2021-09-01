r1 = float(input('Informe o valor da maior reta: '))
r2 = float(input('Informe o valor da reta mediana: '))
r3 = float(input('Informe o valor da menor reta: '))
v1 = r3 + r2
print(' ')
if v1 > r1 and r1 == r2 and r2 == r3 and r1 == r3:
    print('Essas retas formam um triângulo equilátero!')

elif v1 > r1 and r1 == r2 or r2 == r3 or r1 == r3:
    print('Essas retas formam um triângulo isósceles!')

elif v1 > r1 and r1 != r2 and r2 != r3 and r1 != r3:
    print('Essas retas formam um triângulo escaleno!')

else:
    print('Essas retas não formam um triângulo!')
