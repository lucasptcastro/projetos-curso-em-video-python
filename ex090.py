resultado = dict()

resultado['Nome'] = str(input('⏩ Informe o nome do aluno: '))
resultado['Média'] = float(input('⏩ Informe a média do aluno: '))

if resultado['Média'] >= 7:
    resultado['Situação'] = '\033[1;32mAprovado\033[m'
else:
    resultado['Situação'] = '\033[1;31mReprovado\033[m'

print(' ')
print(f'➡ O nome do aluno é {resultado["Nome"]}!')
print(f'➡ A média de {resultado["Nome"]} é {resultado["Média"]}!')
print(f'➡ Sua situação é {resultado["Situação"]}!')
