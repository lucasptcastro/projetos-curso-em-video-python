from modulos.moeda import *


cab('INFO MOEDA')
n = float(input('▶ Informe a quantidade: R$'))
espace()

print(f'▶ O dobro de \033[1;36mR${moedabr(n)}\033[m é \033[1;32mR${moedabr(dobro(n))}\033[m')
print(f'▶ A metade de \033[1;36mR${moedabr(n)}\033[m é \033[1;31mR${moedabr(metade(n))}\033[m')
print(f'▶ Aumentando 10% de \033[1;36mR${moedabr(n)}\033[m têm-se \033[1;32mR${moedabr(aumentar(n))}\033[m')
print(f'▶ Reduzindo 10% de \033[1;36mR${moedabr(n)}\033[m têm-se \033[1;31mR${moedabr(diminuir(n, 25))}\033[m')
