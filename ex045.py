from random import randint
r = str(input('Digite pedra, papel ou tesoura: ')).lower()
ra = randint(1,3)

if r == 'papel' and ra == 1:
    print('O computador escolheu PEDRA! Papel embrulha pedra!')
    print('Você ganhou!')
if r == 'papel' and ra == 2:
    print('O computador escolheu TESOURA! Tesoura corta papel!')
    print('Você perdeu!')
if r == 'papel' and ra == 3:
    print('O computador escolheu PAPEL! Papel não afeta papel!')
    print('Empate!')
if r == 'pedra' and ra == 1:
    print('O computador escolheu PEDRA! Pedra não afeta pedra!')
    print('Empate!')
if r == 'pedra' and ra == 2:
    print('O computador escolheu TESOURA! Pedra quebra tesoura!')
    print('Você ganhou!')
if r == 'pedra' and ra == 3:
    print('O computador escolheu PAPEL! Papel embrulha pedra!')
    print('Você perdeu!')
if r == 'tesoura' and ra == 1:
    print('O computador escolheu PEDRA! Pedra quebra tesoura!')
    print('Você perdeu!')
if r == 'tesoura' and ra == 2:
    print('O computador escolheu TESOURA! Tesoura não afeta tesoura!')
    print('Empate!')
if r == 'tesoura' and ra == 3:
    print('O computador escolheu PAPEL! Tesoura corta papel!')
    print('Você ganhou!')