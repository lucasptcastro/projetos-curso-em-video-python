from random import randint
from random import sample
a1 = 0
ma = a1
me = 11
print('Os valores sorteados foram: ')
for c in range(0,5):
    a1 = randint(0,10)
    print(f'{a1}',end=' ')
    if a1 > ma:
        ma = a1
    if a1 < me:
        me = a1
print(f'\nO maior valor foi: {ma}')
print(f'O menor valor foi: {me}')

#or

print(' ')

a = tuple(sample(range(10),5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}')
