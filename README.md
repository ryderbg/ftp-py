# ftp-py
A FTP client based on python.

## Configuration
Create config.py in src directory with FTP credentials.
Example: 
```
def get_config():
   class Config:
     username = 'python'
     password = '111111111'
     server = '192.168.1.2'
     remote_path = '/archives/new/'
   return Config
```

## Usage

TBD