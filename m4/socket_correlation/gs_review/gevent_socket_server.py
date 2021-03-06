import gevent,socket
from gevent import monkey;monkey.patch_all()

def talk(conn):
    data = conn.recv(1024)
    conn.send(data.upper())

def set_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    while True:
        conn,caddr = server.accept()
        gevent.spawn(talk,conn)

if __name__ == '__main__':
    set_server()