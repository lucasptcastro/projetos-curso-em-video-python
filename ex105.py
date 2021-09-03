def cab(txt):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;37;41m{txt:^48}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

def notas(* valores, sit=False):
    #Variáveis:
    maiorNota = 0
    menorNota = valores[0]
    media = 0
    contNotas = 0
    situacao = str

    #Análise de dados:
    for num in valores:
        media += num
        contNotas += 1
        if num > maiorNota:
            maiorNota = num
        else:
            menorNota = num
    
    #Situacao
    if sit == True:
        if media/contNotas >= 7:
            situacao = 'BOA'
        elif media/contNotas < 7 > 6:
            situacao = "RAZOAVEL"
        else:
            situacao = 'RUIM'
        #Dicionario caso a situacao receba True:
        return {'quantNotas':contNotas, 'maiorNota': maiorNota, 'menorNota': menorNota, 'media': media/contNotas, 'situacao': situacao}
    else:
        #Dicionário
        return {'quantNotas':contNotas, 'maiorNota': maiorNota, 'menorNota': menorNota, 'media': media/contNotas}

#Programa principal
cab('BOLETIM DE ELETRÔNICO')
r = notas(5, 7, 4, 9, sit=True)
print(r)


