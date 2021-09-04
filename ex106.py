def cab(txt):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;37;41m{txt:^48}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

def msg(txt):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[7m{"Acessando o manual do " + txt.upper():^48}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

def ajuda():
    cab("SISTEMA DE AJUDA")
    while True:
        r = str(input('▶ \033[1;32mInforme o comando ao qual você precisa de ajuda:\033[m '))
        if r.upper() == 'FIM':
            return cab("SISTEMA FINALIZADO")
        else:
            msg(r)
            print(f'\033[1;37;41m{r.__doc__}\033[m')
            print(' ')
            continue
        
ajuda()


