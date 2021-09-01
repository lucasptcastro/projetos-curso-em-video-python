from datetime import date
ano = int(input('Informe o ano em que você nasceu: '))
anoa = date.today().year
c = anoa - ano
print(' ')
if c < 17:
    print('\033[34mVocê ainda vai se alistar ao exército!')
    v1 = (17 - c) * 12
    print(f'Ainda faltam {v1} meses para o seu alistamento!\033[m')
elif c == 17:
    print('\033[32mEstá na hora de você se alistar!')
elif c > 17:
    print('\033[31mJá passou da hora de você se alistar!')
    v2 = (c - 17) * 12
    print(f'Seu alistamento está atrasado há {v2} meses!')

