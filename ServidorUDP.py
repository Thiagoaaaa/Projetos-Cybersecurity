import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá cliente, tudo bem?'

while True:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor recebendo dados e enviando resposta...')
        s.sendto((mensagem).encode(), end)

