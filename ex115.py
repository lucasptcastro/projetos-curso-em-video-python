from ex115.modulos import *
from time import sleep

while True:
    quest = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if quest == 1:
        cab('VER PESSOAS CADASTRADAS', 31, 47)
        break
    elif quest == 2:
        cab('CADASTRAR NOVA PESSOA', 31, 47)
        break
    elif quest ==3:
        cab('SAIR DO SISTEMA', 31, 47)
        break
    else:
        print(vermelho('ERRO! DADO INVÁLIDO, TENTE NOVAMENTE!'))
        continue