import config



class BaseApi():
    
    def __init__(self, challenger):
        self.URL = config.URL
        self.status = None
        self.res_body = None
        self.header = {
                'X-CHALLENGER':challenger
            }