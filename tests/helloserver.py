class helloServer:
    def __init__(self):
        pass

    def _hello(self,msg:str):
        print("Get msg : %s" % msg)

    def server(self,msg:str):
        self._hello(msg)
        return f"You sent the message! : {msg}"