import socket

host = '0.0.0.0'
port = 80
s = socket.socket()
s.bind((host, port))

while True:
    s.listen(5)
    connection, address = s.accept()
    print('ip,{}'.format(address))
    response = b'<h1>Hello World!</h1>'
    connection.sendall(response)
    connection.close()
