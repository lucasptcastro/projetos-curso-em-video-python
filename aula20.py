#Comando para definir uma função:
def line():
    print('='*30)

def espace():
    print(' ')

#Função com atribuição de texto:
def título(txt):
    print('='*30)
    print(f'{txt:^30}')
    print('='*30)
título(' HARRY POTTER ')

espace()

#Função com atribuição de soma:
def soma(a,b):
    s = a+b
    print(s)
soma(5,10)

espace()
line()
espace()

#Função com atribuição de soma para vários valores:
def somas(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Os valores {valores} somados são iguais a {s}')
somas(5, 6)
somas(11, 5, 4)

espace()
line()