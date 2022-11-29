import socket 
#ip = socket.gethostbyname('www.google.com')
#print(ip)

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e,org',80))

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
# The encode will update the string into the bytes format.
# Here the string we are sending over is the string inside cmd object.
mysock.send(cmd)

while True:
    data = mysock.recv(512) # The data we recive wil be in bytes
    if(len(data) < 1):
        break
    print(data.decode()) # Here the decode will be changing the bytes data into the string data.

mysock.close()
# The socket connection must be closed.