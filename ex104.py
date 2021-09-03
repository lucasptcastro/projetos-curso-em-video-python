#def leiaInt():
    #while True:
        #a = input('Informe um número: ')
        #if a.isnumeric():
           #return print(f'O número informado foi {a}!')
        #else:
            #continue

#leiaInt()

#ou

def leiaInt(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            return print(f'O número informado foi {n}!')
        else:
            print('Informe um número válido!') 
            continue

n = leiaInt('Informe um número: ') 