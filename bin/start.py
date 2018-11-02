# Author Muse
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import socketserver
from core.server import MyFTPServer
from conf import settings
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(settings.addr, MyFTPServer)
    server.serve_forever()