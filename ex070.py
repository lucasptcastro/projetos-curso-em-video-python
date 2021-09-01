total = 0
mais = 1000
contp = 0
pbarato = 9999999999999999999999999
nomepb = 'a'
while True:
    pdt = str(input('Informe o nome do produto: '))
    preço = float(input('Informe o preço do produto: '))
    total += preço
    if preço > 1000:
        contp += 1
    if preço < pbarato:
        pbarato = preço
        nomepb = pdt
    quest = str(input('Digite C para continuar ou P para parar: ')).upper()
    if quest == 'P':
        break
print(f'O total foi R${total:.2f}')
if contp > 1:
    print(f'{contp} produtos custam mais de R$1000,00!')
if contp == 1:
    print('Apenas um produto custa mais de R$1000,00!')
if contp == 0:
    print('Nenhum produto custa mais de R$1000,00!')
print(f'{nomepb} é o produto mais barato. ')
