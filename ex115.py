from ex115.modulos import *
from time import sleep


arq = 'testeee.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    

while True:
    quest = menu(['Verificar um arquivo', 'Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if quest == 1:
        cab('VERIFICAÇÃO DE ARQUIVOS', 31, 47)
        quest2 = str(input(f'{azul("▶ Informe o nome do arquivo: ")}'))
        if arquivoExiste(quest2):
            sleep(1)
            print(azul(f'O arquivo {quest2} já existe!'))
        else:
            criarArquivo(quest2)
        continue
    elif quest == 2:
        cab('VER PESSOAS CADASTRADAS', 31, 47)
        quest2 = str(input(f'{azul("▶ Informe o nome do arquivo: ")}'))
        lerArquivo(quest2)
        continue
    elif quest == 3:
        cab('CADASTRAR NOVA PESSOA', 31, 47)
        while True:
            quest2 = str(input(f'{azul("▶ Informe o nome do arquivo: ")}'))
            if not arquivoExiste(quest2):
                sleep(1)
                print(vermelho(f'ERRO! O arquivo {quest2} não existe! Tente novamente!'))
                continue
            else:
                break
        nome = str(input(f'{azul("▶ Informe o nome a ser cadastrado: ")}')).title()
        cadastro(quest2, nome, leiaInt(f'{azul("▶ Informe a idade a ser cadastrada: ")}'))
        continue
    elif quest ==4:
        cab('SISTEMA ENCERRADO', 31, 47)
        break
    else:
        print(vermelho('ERRO! DADO INVÁLIDO, TENTE NOVAMENTE!'))
        continue