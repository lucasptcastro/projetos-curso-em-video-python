def leiaInt(a):
    while True:
        if a.isnumeric():
            return
        else:
            continue


#programa principal
n = leiaInt('Digite um número: ')
print(f'O número digitado foi \033[1;36m{n}\033[m!')
