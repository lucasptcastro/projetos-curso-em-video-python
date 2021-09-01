aluno = list()
alunos = list()
id = 0

def espaco ():
    print(' ')

espaco()
print('=-='*15)
print(f'| \033[1:30:46m{"BOLETIM ESCOLAR":^41}\033[m |')
print('=-='*15)
espaco()

while True:
    aluno.append(id)
    aluno.append(input('\033[1:30m⏩ Informe o nome do aluno: \033[m'))
    aluno.append(float(input('\033[1:30m⏩ Informe a\033[m \033[1:33mN1\033[m \033[1:30mdo aluno: \033[m')))
    aluno.append(float(input('\033[1:30m⏩ Informe a\033[m \033[1:33mN2\033[m \033[1:30mdo aluno: \033[m')))
    aluno.append((aluno[2] + aluno[3]) / 2)
    alunos.append(aluno[:])
    aluno.clear()
    id += 1
    quest = str(input('\033[1:30m⏩ Tecle [\033[m\033[1:32mS\033[m\033[1:30m] para adicionar mais um ou [\033[m\033[1:31mP\033[m\033[1:30m] para parar: \033[m')).upper()
    if quest != 'S':
        break
    else:
        continue

espaco()
print('=-='*15)
print(f'| \033[1:30:46m{"RESULTADO FINAL":^41}\033[m |')
print('=-='*15)
espaco()

print(f'ID {"Nome":^5} {"Media":^30}')

for c in range(0, len(alunos)):
    print(f'{alunos[c][0]:<}  {alunos[c][1]:<5} {alunos[c][4]:^30}')

espaco()
print('=-='*25)

while True:
    quest2 = input(f'\033[1:30m⏩ Informe o ID do aluno para realizar a consulta de notas (000 para): \033[m')
    quest3 = int(quest2)
    if quest2 == '000':
        print('=-=' * 15)
        print(f'| \033[1:30:41m{"PROGRAMA ENCERRADO":^41}\033[m |')
        print('=-=' * 15)
        break
    else:
        print(f'\033[1:30m⏩\033[m As notas de {alunos[quest3][1]} foram: {alunos[quest3][2]}, {alunos[quest3][3]}')
        continue


