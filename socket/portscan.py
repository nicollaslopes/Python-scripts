import socket

ip = input('Digite o IP: ')
p = int(input('Digite o numero de portas que deseja scanear: '))
portas = []

for i in range(p):
    portas.append(int(input('Digite a porta: ')))

for port in portas:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.6)
    code = client.connect_ex((ip, port))
    if code == 0:
        print ('Porta -> ' + str(port) + ' aberta!')
    else:
        print('Porta -> ' + str(port) + ' fechada...')

print('Scan finalizado.')
