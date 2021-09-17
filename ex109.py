from modulos.moeda import *


cab('INFO MOEDA')
n = float(input('▶ Informe a quantidade: R$'))
espace()

print(f'▶ O dobro de \033[1;36m {moedabr(n)}\033[m é \033[1;32m{moedabr(dobro(n), False)}\033[m')
print(f'▶ A metade de \033[1;36m{moedabr(n)}\033[m é \033[1;31m{moedabr(metade(n))}\033[m')
print(f'▶ Aumentando 10% de \033[1;36m{moedabr(n)}\033[m têm-se \033[1;32m{moedabr(aumentar(n), False)}\033[m')
print(f'▶ Reduzindo 10% de \033[1;36m{moedabr(n)}\033[m têm-se \033[1;31m{moedabr(diminuir(n, 10))}\033[m')