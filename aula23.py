#Comando a qual deve estar a operação
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

#Comando para caso aconteça um erro
except Exception as erro:
    print(f'O problema encontrado foi: {erro.__class__}')

#Comando para caso não aconteça um erro
else:
    print(f'O resultado é {r}')

#Comando que SEMPRE irá acontecer, independente de erro ou não
finally:
    print('Obrigado por usar o sistema! Volte sempre :)')