from werkzeug.security import safe_str_cmp
from UserValidator import UserValidator

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

users = [
    User(1, 'karim@template.be', 'pass'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

class AuthenticateUserQuery:


        def __init__ (self):
            self.validator= UserValidator()


        def authenticate(self, username, password):
            print(username)
            print(password)
            valid=self.validator.validate(username, password)
            if valid:
                user = username_table.get(username, None)
                if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
                    return user
            return False

        def identity(self, payload):
            user_id = payload['identity']
            print(user_id)
            return userid_table.get(user_id, None)