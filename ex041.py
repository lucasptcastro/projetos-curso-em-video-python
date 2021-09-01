from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
anoa = date.today().year
c = anoa - ano

if c <= 9:
    print('Sua categoria é \033[36mMIRIM\033[m!')
elif c > 9 and c <= 14:
    print('Sua categoria é \033[34mINFANTIL\033[m!')
elif c > 14 and c <= 19:
    print('Sua categoria é \033[32mJUNIOR\033[m!')
elif c > 19 and c <= 20:
    print('Sua categoria é \033[33mSÊNIOR\033[m!')
elif c > 20:
    print('Sua categoria é \033[31mMASTER\033[m!')
