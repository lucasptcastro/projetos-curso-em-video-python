from modulos.cores import vermelhoN
from modulos.moeda import *

#Cabeçalho
cab("ENTRADA DE DADOS")

#Função para leitura de números inteiros
def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(vermelhoN("ERRO! Por favor, informe um número inteiro válido!"))
            continue
        except (KeyboardInterrupt):
            print(vermelhoN("\nERRO! Nenhuma entrada de dados informada!"))
            return 0
        else:
            return n
            
#Função para leitura de números reais
def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print(vermelhoN("ERRO! Por favor, informe um número real válido!"))
            continue
        except (KeyboardInterrupt):
            print(vermelhoN("\nERRO! Nenhuma entrada de dados informada!"))
            return 0
        else:
            return n

#Leitura de dados
i = leiaInt('▶ Informe um número inteiro: ')
f = leiaFloat('▶ Informe um número real: ')

#Cabeçalho
cab("PROGRAMA ENCERRADO")
#Impressão de dados
print(f'▶ O valor inteiro informado foi {i} e o real {f}')
#Espaço
espace()