

class ClientDb(self):
    def __init__(self):
        raise NotImplementedError

    def translate_login_to_usertoken(self, userlogin):
        raise NotImplementedError

    def fetch_basket_sessions(self, userid):
        raise NotImplementedError