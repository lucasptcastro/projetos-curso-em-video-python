from random import randint
cont = 0
while True:
    n1 = int(input('Digite um valor: '))
    question = str(input(('Você quer I ou P: '))).upper()
    pi = randint(0, 10)
    soma = (n1 + pi) % 2
    if question == 'P':
        if soma == 0:
            print(f'O computador escolheu {pi} e você {n1}! A soma entre os números é PAR! Você acertou!')
            cont += 1
        if soma == 1:
            print(f'O computador escolheu {pi} e você {n1}! A soma entre os números é ÍMPAR! Você errou!')
            print(f'Seu total de acertos consecutivos foi {cont}!')
            break
    if question == 'I':
        if soma == 1:
            print(f'O computador escolheu {pi} e você {n1}! A soma entre os números é ÍMPAR! Você acertou!')
            cont += 1
        if soma == 0:
            print(f'O computador escolheu {pi} e você {n1}! A soma entre os números é PAR! Você errou!')
            print(f'Seu total de acertos consecutivos foi {cont}!')
            break