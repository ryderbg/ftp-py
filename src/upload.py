import os
from helpers.get_dir_name import get_dir_name 
from config import get_config

def upload(session, local_path):
    files = os.listdir(local_path)
    os.chdir(local_path)
    print(files)
    for f in files:
        if os.path.isfile(local_path + r'\{}'.format(f)):
            fh = open(f, 'rb')
            session.storbinary('STOR %s' % f, fh)
            fh.close()
            print(f)
        elif os.path.isdir(local_path + r'\{}'.format(f)):
            session.mkd(f)
            session.cwd(f)
            upload(session, local_path + r'\{}'.format(f))
            print(f)
    session.cwd('..')
    os.chdir('..')

