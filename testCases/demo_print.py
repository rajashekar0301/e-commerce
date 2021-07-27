import configparser
from configparser import ConfigParser




config=configparser.ConfigParser()
# config.read('sampleconfig.ini')
config.read('..\Configurations\config.ini')

for sect in config.sections():
    print('Section:',sect)
    print(config.get(sect,'baseurl'))
    for k,v in config.items(sect):
        print('{}={}'.format(k,v))
    print()

