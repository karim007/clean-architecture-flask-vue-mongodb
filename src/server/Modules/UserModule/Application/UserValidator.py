

class UserValidator:

    def validate(self, user, password):

        resp= True  if user and password else False
        print(resp)
        return resp

