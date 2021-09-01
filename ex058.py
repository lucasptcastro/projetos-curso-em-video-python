import random
c = 0
print('O computador irá escolher aleatoriamente um número entre 0 e 10. Seu dever é descobrir qual foi o número escolhido.')
na = random.randrange(0,10)
r = int(input('Informe o número que você acredita ser o certo: '))
while r != na:
    r = int(input('Você errou! Tente novamente: '))
    c += 1
if c == 0:
    print(f'===|=== Parabéns, você acertou! O número correto era {na}! Você não errou nenhuma vez! ===|===')
if c == 1:
    print(f'===|=== Parabéns, você acertou! O número correto era {na}! Você errou {c} vez! ===|===')
else:
    print(f'===|=== Parabéns, você acertou! O número correto era {na}! Você errou {c} vezes! ==|==')
