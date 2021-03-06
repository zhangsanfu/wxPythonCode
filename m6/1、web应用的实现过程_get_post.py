import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8800))
server.listen(5)

while 1:
    print('waiting')
    conn,caddr = server.accept()
    data = conn.recv(1024)
    print(data)
    # 添加html标签样式后，浏览器会渲染字符串中的标签样式
    with open('./temples/login.temples','rb') as f:
        fdata = f.read()
        print(fdata)
    conn.send((b'HTTP1.1 200 OK\r\nContent-type:text/temples\r\n\r\n')+fdata)
    conn.close()