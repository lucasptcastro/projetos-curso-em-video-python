words = 'Piano', 'Labirintite', 'Mouse', 'Teto', 'Feijão', 'Paralelepipedo', 'Formiga', 'Fogareu', 'Nuvem'
for c in words:
    print(f'\nNa palavra \033[32m{c:<5}\033[m temos ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'\033[33m{letra}\033[m',end=' ')


