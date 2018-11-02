# Author Muse
import json
import socketserver
from core import views
from conf import settings
class MyFTPServer(socketserver.BaseRequestHandler):
    logined_lst = {}
    def handle(self):
        while True:
            msg = self.my_recv()
            print(MyFTPServer.logined_lst)
            op_str = msg['operation']
            if msg['operation'] == 'login' or msg['operation'] == 'register':
                if hasattr(views,op_str):
                    func=getattr(views,op_str)
                    ret,pickle_path = func(msg)
                if ret == True:
                    MyFTPServer.logined_lst[self.client_address] = pickle_path#用户的pickle信息所在的文件地址
                    self.my_send(ret)
            elif hasattr(views,op_str) and self.client_address in MyFTPServer.logined_lst:
                func = getattr(views, op_str)
                ret = func(msg,self.request)
                self.my_send(ret)
            else:
                self.my_send(False)

    def my_recv(self):
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        print(msg,type(msg))
        msg = json.loads(msg)
        return msg

    def my_send(self,msg):
        msg = json.dumps(msg).encode(settings.code)
        self.request.send(msg)