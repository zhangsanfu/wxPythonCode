import socket
import sys
import os
import json
import struct

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from core import login
from setting import set_struct
from setting import set_file
from setting import set_md5

class FTPServer:
    reuse_addr = True
    max_queue_size = 5
    max_recv_size = 8192
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.encoding = sys.getdefaultencoding()

    def server_bind(self):
        self.server.bind((self.host,self.port))
        if self.reuse_addr:
            self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def server_listen(self):
        self.server.listen(self.max_queue_size)

    def server_accept(self):
        self.conn, self.caddr = self.server.accept()
        while True:
            login_info = set_struct.struct_unpack(self.conn)
            if login_info == None:
                break

            issuccess,self.username = login_obj.login(login_info)
            set_struct.struct_pack(self.conn, issuccess)
            if issuccess == True:
                print('账户验证成功，服务端准备就绪...')
                return
            else:
                print('账户验证失败，服务端重置连接...')
                continue

    def get(self):
        pass

    def put(self,filename):
        put_file_dict = set_struct.struct_unpack(self.conn)
        puted_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,filename)
        recv_size = 0
        recv_rate = 0

        if os.path.exists(puted_file):
            puted_file_md5 = set_md5.set_file_md5(puted_file)
            print(puted_file_md5)
            print(put_file_dict['file_md5'])
            if puted_file_md5 == put_file_dict['file_md5']:
                put_dict = {
                    'put_status':False,
                    'put_message':'您的云空间中已存在该文件'
                }
                set_struct.struct_pack(self.conn,put_dict)
                return
        else:
            f = set_file.write_file(puted_file,'wb')
            while recv_size < put_file_dict['file_size']:
                data = self.conn.recv(self.max_recv_size)
                f.write(data)
                recv_size += len(data)
                print(recv_size,put_file_dict['file_size'])
                recv_rate = round(recv_size / put_file_dict['file_size'],2)*100
                print('上传进度%s'%recv_rate+'%')
        return

    def run(self):
        self.server_bind()
        self.server_listen()
        while True:
            self.server_accept()
            while True:
                # try:
                cmd = self.conn.recv(self.max_recv_size)
                if not cmd:
                    print('客户端关闭，服务端重置连接')
                    break
                request_method = cmd.decode(self.encoding).split()[0]
                request_content = cmd.decode(self.encoding).split()[1]

                if hasattr(self,request_method):
                    func = getattr(self, request_method)
                    func(request_content)
                    continue
                self.conn.close()
                # except ConnectionResetError as e:
                #     print(e)
                #     break


if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8081)
    print('请先登录...')
    login_obj = login.UserBehavior()
    f.run()




