# import configparser
import configparser
from configparser import ConfigParser
# config=configparser.RawConfigParser()
# config.read('..\Configurations\sampleconfig.ini')

config=configparser.ConfigParser()
config.read('..\Configurations\config.ini')

# for sect in config.sections():
#     print('Section:',sect)
#     print(config.get(sect,'baseurl'))
#     for k,v in config.items(sect):
#         print('{}={}'.format(k,v))
#     print()

class ReadConfig():
    # to access method (getApplicationURL) directly using class (ReadConfig), we have define as Staticmethod
    @staticmethod
    def getApplicationURL():
        for sect in config.sections():
            url=config.get(sect,'baseurl')
            print(url)
            return url
        # url=config.get('common info','baseURL')
    @staticmethod
    def getUseremail():
        for sect in config.sections():
            username=config.get(sect,'username')
            print(username)
            return username
        # username=config.get('common info','username')
        # return username

    @staticmethod
    def getPassword():
        for sect in config.sections():
            password=config.get(sect,'password')
            print(password)
            return password
        # password=config.get('common info','password')
        # return password

