from modulos.uteis import cab


def dobro(n):
    return n*2

def metade(n):
    return n/2

def aumentar(n, n2=10):
    a = (n*n2) / 100
    return n + a

def diminuir(n, n2=13):
    d = (n*n2) / 100
    return n - d

def moedabr(n, format=True):
    if format == False:
        return n
    else:
        return f'R${n:.2f}'.replace('.',',')

def resumo(n=0, aum=0, red=0):
    cab("RESUMO FINANCEIRO")
    print(f'Preço analisado: {" "*15} \t{moedabr(n)}')
    print(f'Dobro do preço: {" "*15} \t{moedabr(dobro(n))}')
    print(f'Metade do preço: {" "*15} \t{moedabr(metade(n))}')
    print(f'\033[1;32m{aum}%\033[m de aumento: {" "*15} \t{moedabr(aumentar(n, aum))}')
    print(f'\033[1;31m{red}%\033[m de redução: {" "*15} \t{moedabr(diminuir(n, red))}')
    cab("ENCERRADO")
