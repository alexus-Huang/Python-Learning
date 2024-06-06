class Login:
    def __init__(self,login_attempts):
        self.login_attempts = login_attempts
    
    def login_attempt(self,increase):
        self.login_attempts += increase
    
    def reset_login_attempts(self):
        self.login_attempts = 0


new_login = Login(0)

print(new_login.login_attempts)

new_login.login_attempt(1)

print(new_login.login_attempts)

new_login.login_attempt(1)

print(new_login.login_attempts)

new_login.reset_login_attempts()

print(new_login.login_attempts)