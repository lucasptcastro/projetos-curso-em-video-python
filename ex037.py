n = int(input('Informe um número inteiro: '))
print('Tecle [1] para converter para binário')
print('Tecle [2] para converter para octal')
print('Tecle [3] para converter para hexadecimal')
print(' ')
r = int(input('Informe aqui sua escolha: '))

if r == 1:
    print(f'O valor em binário é {bin(n)[2:]}')
elif r == 2:
    print(f'O valor em octal é {oct(n)[2:]}')
elif r == 3:
    print(f'O valor em hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida!')
