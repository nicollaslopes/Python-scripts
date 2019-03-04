import dns.resolver
import sys

print('>>>>>>>>>>>> MODO DE USAR: python dnsbrute.py <dominio> <wordlist> ')

try:
    dominio = sys.argv[1]
    arquivo = sys.argv[2]
except:
    print ('Argumentos invalidos!')

try:
    arquivo = open(arquivo)
    subDominios = arquivo.read().splitlines()
except:
    print('Arquivo nao encontrado...')
    sys.exit()

for subDominio in subDominios:
    try:
        domESub = subDominio + '.' + dominio
        resultados = dns.resolver.query(domESub, 'a')
        for resultado in resultados:
            print("Subdomonio: ", domESub, "| IP: ->", resultado)
    except:
        pass

