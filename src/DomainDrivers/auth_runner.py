
class Authenticator():
    def __init__(self):
        raise NotImplementedError

    def reload_database(self):
        raise NotImplementedError

    def AddUser(
        self, 
        user_login : str, 
        user_password : str, 
        user_email : str
    ):
        raise NotImplementedError

    def AuthUser(
        self, 
        user_login : str, 
        user_password : str
    ):
        raise NotImplementedError

    def ResetPasswd(self, user_hint : str):
        raise NotImplementedError