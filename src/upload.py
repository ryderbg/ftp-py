import os
import ftplib
from helpers.get_dir_name import get_dir_name 
from config import get_config

path = r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'

dir_name = get_dir_name(path)
config = get_config()

session = ftplib.FTP(config.server, config.username, config.password)
session.cwd(config.remote_path)
session.mkd(dir_name)
session.cwd(dir_name)

def upload(local_path):
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
            upload(local_path + r'\{}'.format(f))
            print(f)
    session.cwd('..')
    os.chdir('..')
upload(path)

