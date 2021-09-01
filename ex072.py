numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
n1 = int(input('Informe um número entre 0 e 20: '))
for c in numeros:
    if n1 > 20:
        n1 = int(input('Tente novamente! Informe um número entre 0 e 20: '))
    else:
        print(f'A forma por extenso do número {n1} é {numeros[n1]}!')
        break