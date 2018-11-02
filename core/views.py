# Author Muse
import os
import pickle
from core.user import User
from conf import settings
def login(msg):
    # wait completed later
    print(msg)

def register(msg):
    user_obj = User(msg['username'])
    pickle_path = os.path.join(settings.pickle_path,msg['username'])
    with open(pickle_path,'wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)
    with open(settings.user_info,'a') as f:
        f.write('%s|%s|%s\n'%(msg['username'],msg['password'],pickle_path))
    return True,pickle_path

def upload(msg,request):
    # wait completed
    print(msg)

def download(msg):
    # wait completed
    print(msg)
