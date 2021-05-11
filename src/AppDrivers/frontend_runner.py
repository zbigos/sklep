

class FrontendRunner:
    def __init__(self, userID):
        raise NotImplementedError

    async def ParseCMD(self, arg):
        raise NotImplementedError

    async def TelnetRunner(self):
        raise NotImplementedError