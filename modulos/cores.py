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


