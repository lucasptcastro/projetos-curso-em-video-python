cont = 0
numbers = []
maior = 0
menor = 9999999999
for c in range (0,5):
    n1 = int(input(f'Informe um número na posição {cont}: '))
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    cont += 1
    numbers.append(n1)
print(f'Você informou os valores: {numbers}')

print(' ')
print('-'*18,'|','-'*18)
print(' ')

print(f'O maior número informado foi {maior} na posição ', end='')
for i, v in enumerate(numbers):
    if v == maior:
        print(f'{i}...')
print(f'O menor número informado foi {menor} na posição ', end='')
for i, v in enumerate(numbers):
    if v == menor:
        print(f'{i}...')
