import ftplib
from config import get_config
from helpers.get_dir_name import get_dir_name
from upload import upload 

path = r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'

dir_name = get_dir_name(path)
config = get_config()

session = ftplib.FTP(config.server, config.username, config.password)
session.cwd(config.remote_path)
session.mkd(dir_name)
session.cwd(dir_name)


upload(session, path)
