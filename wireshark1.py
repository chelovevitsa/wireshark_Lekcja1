# socket -> TCP
# IPlokalne
# IPdocelowe
# -> <-
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('www.httpbin.org', 80))
# s.sendall('GET /html HTTP/1.1\r\nHost: httpbin.org\r\n\r\n'.encode('utf-8'))
# data = s.recv(1).decode('utf-8')
# html = data.split('\r\n\r\n')[1]
# with open('index.html', 'w') as f:
#     f.write(html)
# print('SAVED')
# s.close()
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.httpbin.org', 80))
s.sendall('GET /html HTTP/1.1\r\nHost: httpbin.org\r\n\r\n'.encode('utf-8'))


data = b''
while b'\r\n\r\n' not in data:
    data += s.recv(100)

contentlength = int(data.decode('utf-8').split('Content-Length: ')[1].split('\r\n')[0])

header_length = len(data.decode('utf-8').split('\r\n\r\n')[0])

while len(data) < contentlength + header_length:
    data += s.recv(100)
    

data = data.decode('utf-8')

print(data.split('\r\n\r\n')[0])

with open('index.html', 'w') as f:
    f.write(data.split('\r\n\r\n')[1])
