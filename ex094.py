pessoas = dict()
persons = list()
calc = calcM = 0

def espace():
    print(' ')

espace()
print('='*50)
print(f'|\033[1:30:42m{"COLETA DE DADOS":^48}\033[m|')
print('='*50)

while True:
    pessoas['name'] = str(input('⏩ Informe o nome: ')).lower().title()
    while True:
        pessoas['sex'] = str(input('⏩ Use "M" para masculino e "F" para feminino: ')).upper()
        if pessoas['sex'] in 'MF':
            break
        print('\033[1:31m ERRO! Coloque uma informação válida! \033[m')
    pessoas['age'] = int(input('⏩ Informe a idade: '))
    persons.append(pessoas.copy())
    espace()
    while True:
        quest = str(input('⏩ Informe "C" para continuar ou "P" para parar: ')).upper()
        if quest in 'CP':
            break
        print('\033[1:31m ERRO! Coloque uma informação válida! \033[m')
    espace()
    if quest == 'P':
        break
    else:
        continue

espace()
print('='*50)
print(f'|\033[1:30:44m{"INFORMAÇÕES":^48}\033[m|')
print('='*50)

#PessoasCadastradas
print(f'▶ Foram cadastradas \033[1:34m{len(persons)}\033[m pessoas!')

#MédiaIdade
for c, v in enumerate(persons):
    calc = calc + persons[c]['age']
print(f'▶ A média etária do grupo é igual a \033[1:34m{calc / len(persons):.0f}\033[m!')

#ListaMulheres
print(f'▶ As mulheres incluídas foram:')
for c, v in enumerate(persons):
    if persons[c]['sex'] == 'F':
        print(f'{"🔵 ":>5}\033[1:33m{persons[c]["name"]:<}\033[m')

#PessoasAcimaDaMédia
print(f'▶ As pessoas com idade acima da média são:')
for c, v in enumerate(persons):
    if persons[c]['age'] > calc/len(persons):
        print(f'{"🔵 ":>5}\033[1:33m{persons[c]["name"]:<}\033[m')

#ProgramaEncerrado
print('='*50)
print(f'|\033[1:30:41m{"PROGRAMA ENCERRADO":^48}\033[m|')
print('='*50)