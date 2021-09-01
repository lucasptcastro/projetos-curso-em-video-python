from datetime import date

#espaço
def espace():
    print(" ")

#cabeçalho
def cab(txt):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;37;41m{txt:^48}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

#voto
def voto():
    espace()
    ano = int(input('▶ Informe o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 17 and idade < 65:
        return f'     Sua idade é {idade} anos! Logo, o voto é \033[1;32mOBRIGATÓRIO!\033[m'
    elif idade < 17:
        return f'     Sua idade é {idade} anos! Logo, o voto está \033[1;31mNEGADO!\033[m'
    else:
        return f'     Sua idade é {idade} anos! Logo, o voto é \033[1;36mOPCIONAL!\033[m'

espace()
cab("ANÁLISE DE VOTO")
print(voto())
espace()