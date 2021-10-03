#Cores
def vermelho(txt, fundo=40):
    return f'\033[1;31;{fundo}m{txt}\033[m'

def verde(txt, fundo=40):
    return f'\033[1;32;{fundo}m{txt}\033[m'

def branco(txt, fundo=40):
    return f'\033[1;{fundo}m{txt}\033[m'

def amarelo(txt, fundo=40):
    return f'\033[1;33;{fundo}m{txt}\033[m'

def azul(txt, fundo=40):
    return f'\033[1;36;{fundo}m{txt}\033[m'

#Interface
def cab(txt, cor=37, fundo=41):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;{cor};{fundo}m{txt.center(48)}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

def espace():
    print(' ')

def linha(i=50):
    print('='*i)

def menu(lista):
    cab("INTERFACE PYTHON", cor=37, fundo=41)
    c = 1
    for item in lista:
        print(f'{amarelo(c)} - {verde(item)}')
        c+=1
    linha()
    question = leiaInt(azul("▶ Informe sua opção: "))
    return question

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(vermelho("ERRO! Por favor, informe um número inteiro válido!"))
            continue
        except (KeyboardInterrupt):
            print(vermelho("\nERRO! Nenhuma entrada de dados informada!"))
            return 0
        else:
            return n


