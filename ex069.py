maior = 18
cidade = 0
cm = 0
cf = 0
while True:
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Digite M para masculino e F para feminino: ')).upper()
    if idade > maior:
        cidade += 1
    if sexo == 'M':
        cm += 1
    if sexo == 'F' and idade < 20:
        cf += 1
    cont = str(input('Digite C para continuar ou P para parar: ')).upper()
    if cont == 'P':
        break
print(f'Há {cidade} pessoas com mais de 18 anos! Foram cadastrados {cm} homens! Há {cf} mulheres com menos de 20 anos!')


