from modulos.moeda import *


cab('INFO MOEDA')
n = float(input('▶ Informe a quantidade: R$'))
espace()

print(f'▶ O dobro de \033[1;36mR${n:.2f}\033[m é \033[1;32mR${dobro(n):.2f}\033[m')
print(f'▶ A metade de \033[1;36mR${n:.2f}\033[m é \033[1;31mR${metade(n):.2f}\033[m')
print(f'▶ Aumentando 10% de \033[1;36mR${n:.2f}\033[m têm-se \033[1;32mR${aumentar(n):.2f}\033[m')
print(f'▶ Reduzindo 10% de \033[1;36mR${n:.2f}\033[m têm-se \033[1;31mR${diminuir(n, 10):.2F}\033[m')