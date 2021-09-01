casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos gostaria de pagar: '))

v1 = anos * 12
p = casa / v1
pe = (30*salario) / 100
vt = pe+p

print(' ')

if vt < salario:
    print(f'As parcelas a serem pagas serão no valor de R${p:.2f} mensais!')

elif salario < vt:
    print(f'Empréstimo negado! Você, infelizmente, não pode pagar por esta casa!')
#print(f'{v1}')
#print(f'{p:.2f}')
#print(f'{pe}')
