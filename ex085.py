numeros = [[],[]]
maior = 0
menor = 0
cont = 1
def espaco():
    print(' ')
espaco()
for c in range(0,7):
    pergunta = int(input(f'Informe o {cont}° número: '))
    if pergunta % 2 == 0:
        numeros[0].append(pergunta)
    else:
        numeros[1].append(pergunta)
    cont += 1
numeros[0].sort()
numeros[1].sort()
espaco()
print(f'Os números pares informados foram: {numeros[0]}')
print(f'Os números ímpares informados foram: {numeros[1]}')