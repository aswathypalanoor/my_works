import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('Login Info','admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('Login Info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Login Info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        inv_username = config.get('Login Info', 'invalid_username')
        return inv_username