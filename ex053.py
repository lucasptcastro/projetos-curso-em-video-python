f = str(input('Digite uma frase para saber se é um políndromo: ')).strip()
d = f.split()
d1 = ''.join(f)
d2 = ' ' in f
if d2 == True:
    