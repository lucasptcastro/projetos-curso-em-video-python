dados = list ()
pessoas = list()
pesomaior = pesomenor = 0.0
cont = 0

def espaco():
    print(' ')

print('=-='*10)
print('| ', f'{"Cadastro de pessoas":^25}', '|')
print('=-='*10)

while True:
    espaco()
    dados.append(str(input('Informe o nome: ')))
    dados.append(float(input('Informe o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    espaco()
    pergunta = input('Use [C] para continuar ou [P] para parar: ').upper()
    if pergunta == 'C':
        continue
    elif pergunta == 'P':
        break
    elif pergunta != 'C' and 'P':
        espaco()
        print('\033[1;33mComando inválido! Tente novamente!\033[m')
        espaco()
        perguntaerro = input('Use [C] para continuar ou [P] para parar: ').upper()
        if perguntaerro == 'C':
            continue
        elif perguntaerro == 'P':
            break
        elif perguntaerro != 'C' and 'P':
            espaco()
            print('\033[1;31mComando inválido novamente! Programa encerrado!\033[m')
            break

print(pessoas)
espaco()

print('=-='*11)
print('| ', f'\033[1;32m{"Cadastro finalizado":^27}\033[m', ' |')
print('=-='*11)

if len(pessoas) > 1:
    print('| ', f'{"Foram cadastradas":<10}', f'{len(pessoas):^}',"pessoas", f'{" |":2>}')
if len(pessoas) == 1:
    print('| ', f'{"Foi cadastrada uma pessoa":^27}', ' |')

for p in pessoas:
    if p[1] > pesomaior:
        pesomaior = p[1]
print(f"O maior peso informado foi de \033[34m{pesomaior}\033[mKg's! Pertencentes a", end=' ')
for p in pessoas:
    if p[1] == pesomaior:
        print(f'{p[0]} ', end='')
print()
pesomenor = pesomaior
for p in pessoas:
    if p[1] < pesomenor:
        pesomenor = p[1]
print(f"O menor peso informado foi de \033[34m{pesomenor}\033[mKg's! Pertencentes a", end=' ')
for p in pessoas:
    if p[1] == pesomenor:
        print(f'{p[0]} ', end='')
print()