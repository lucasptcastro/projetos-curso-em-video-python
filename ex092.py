worker = dict()
print(' ')
worker['nome'] = str(input('Informe o seu nome: ')).title()
worker['date'] = int(input('Informe o seu ano de nascimento: '))
worker['ctps'] = int(input('Informe o número da sua CTPS: '))


if worker['ctps'] == 0:
    print(' ')
    print(f'O seu nome é \033[1:32m{worker["nome"]}\033[m!')
    print(f'O seu ano de nascimento é \033[1:32m{worker["date"]}\033[m!')
    print(f'O número da sua CTPS é \033[1:32m{worker["ctps"]}\033[m!')

else:
    worker['yearOfContratation'] = int(input('Informe o ano de contratação: '))
    worker['wage'] = float(input('Informe o seu salário: '))
    worker['retirement'] = (worker['yearOfContratation'] + 35) - worker['date']
    print(' ')
    print(f'O seu nome é \033[1:32m{worker["nome"]}\033[m!')
    print(f'A sua data de nascimento é \033[1:32m{worker["date"]}\033[m!')
    print(f'O número da sua CTPS é \033[1:32m{worker["ctps"]}\033[m!')
    print(f'Você foi contratado no ano de \033[1:32m{worker["yearOfContratation"]}\033[m!')
    print(f'Seu salário é igual a \033[1:34mR${worker["wage"]:.2f}\033[m!')
    print(f'Você ira se aposentar com \033[1:32m{worker["retirement"]}\033[m anos!')
