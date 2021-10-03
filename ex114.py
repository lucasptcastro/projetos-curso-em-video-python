import urllib #módulo que trabalha com url's
import urllib.request

#Programa pra ver se o site está funcionando
try:
    #Comando para abrir o site
    site = urllib.request.urlopen('https://www.facebook.com')
except:
    print('Deu erro')
else:
    print('Tudo ok')