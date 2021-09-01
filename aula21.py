#=== INTERACTIVE HELP ===#

print(' ')
print('\033[4;31;47m° Interactive Help:\033[m')
print(' ')

#Saber a definição de um comando:
help(print)
#Ou
print(input.__doc__)

#=== DOCSTRINGS ===#

print(' ')
print('\033[4;31;47m° Docstrings:\033[m')
print(' ')

#Para documentar uma função:
def soma(a, b, c):
    """
    Essa funcao soma 3 parametros: a, b e c
    """
    s = a+b+c
    print(f'A soma dos números informados é {s}')
soma(5, 5, 10)
help(soma)

#=== PARÂMETROS OPCIONAIS ===#

print(' ')
print('\033[4;31;47m° Parâmetros Opcionais:\033[m')
print(' ')

#Para tornar um parâmetro opcional:
def somas(a, b, c=0): #basta colocar =(numero que voce quer que apareça caso não seja colocado nada no parametro) ao lado do parâmetro
    s = a + b + c
    print(f'A soma dos resultados informados é igual a {s}')
somas(3, 2)

#=== ESCOPO DE VARIÁVEIS ===#

print(' ')
print('\033[4;31;47m° Escopo de Variáveis:\033[m')
print(' ')

#Para transformar uma váriavel local em global:
def teste(b):
    global a #basta usar o "global" antes da variável
    a = 8
    b+=4
    c = 2
    print(f'O novo valor de A é: {a}')
    print(f'O valor de B é: {b}')
    print(f'O valor de C é: {c}')
a = 5
print(f'O valor de A é: {a}')
teste(a)

#=== RETORNANDO VALORES ===#

print(' ')
print('\033[4;31;47m° Retornando Valores:\033[m')
print(' ')

#Para retornar um valor para uma variável:
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s #S vai retornar ao que está antes do def, no caso, r1, r2 e r3


r1 = somar(3, 4, 5)
r2 = somar(1, 3)
r3 = somar(2)

print(f'Meus cálculos deram {r1}, {r2} e {r3}!')