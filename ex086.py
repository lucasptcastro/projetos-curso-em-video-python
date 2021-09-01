#coluna1 = list()
#coluna2 = list()
#coluna3 = list()
#cont = 0

#def espaco():
#    print(' ')

#for c in range(0,3):
 #   coluna1.append(input(f'Digite um valor para [0, {cont}]: '))
  #  cont += 1

#for c in range(0,3):
 #   coluna2.append(input(f'Digite um valor para [1, {cont}]: '))
  #  cont += 1

#for c in range(0,3):
 #   coluna3.append(input(f'Digite um valor para [2, {cont}]: '))
  #  cont += 1


#for c in range(0,3):
  #  print(f'[{coluna1[cont]}]', end=' ')
 #   cont += 1

# ou

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for p in range (0,3):
    for c in range(0,3):
        matriz[p][c] = int(input(f'Digite um valor para [{p}, {c}]: '))
for p in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[p][c]:^5}]', end='')
    print()
