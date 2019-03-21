

class Login(object):
    
    def __init__(self):
        self.headers = {

        }
        self.login_url = ''
        self.post_url = ''
        self.logined_url = ''
        self.session = request.Session()