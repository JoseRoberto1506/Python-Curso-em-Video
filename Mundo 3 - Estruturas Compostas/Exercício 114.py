'''Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.'''

# Importar biblioteca urllib e o módulo interno request
import urllib
import urllib.request

try:
    # Abrir URL
    site = urllib.request.urlopen("http://www.pudim.com.br")
# Exceção padrão
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Site acessado com sucesso!')
