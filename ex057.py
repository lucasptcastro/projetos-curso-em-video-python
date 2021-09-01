s = str(input('Digite M para Masculino ou F para Feminino: ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Código inválido! Informe F para Feminino ou M para Masculino: '))
print(f'O gênero selecionado foi: {s.upper()}!')