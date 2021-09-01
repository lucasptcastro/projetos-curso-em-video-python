cont = 0
lista = list()
r = 1
add5 = 0
def linha():
    print(' ')

print('-'*10, end='')
print(f'{"Lista de números variados":^27}', end='')
print('-'*10)

linha()

lista.append(int(input('Para começar, informe um número para ser adicionado na lista: ')))
cont = cont + 1

linha()

while r != 0:
    question = int(input('Para adicionar um número digite [1], digite [0] para parar: '))
    if question == 1:
        add = int(input('Informe o número a ser adicionado na lista: '))
        lista.append(add)
        cont = cont + 1
        r == 1
        if add == 5:
            add5 = add5 + 1
    if question == 0:
        linha()
        print('-'*10, end='')
        print(f'{"Programa encerrado":^20}', end='')
        print('-' * 10)
        linha()
        print(f'➡ Foram digitados {cont} números!')
        lista.sort(reverse=True)
        print(f'➡ Esta é a lista em forma decrescente: {lista}')
        if add5 >= 1:
            print('➡ O valor 5 foi digitado e está na lista.')
        else:
            print('➡ O valor 5 não foi digitado!')
        break