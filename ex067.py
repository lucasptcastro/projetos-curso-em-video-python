while True:
    n1 = int(input('Informe o número para saber a tabuada: '))
    if n1 < 0:
        print('Programa Encerrado!')
        break
    for c in range(1,11):
        print(f'|{n1} x {c} = {n1*c}|')

