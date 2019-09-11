
from ..Infrastucture.DataBase import Repository, FakeRepository

class TechniquesQueries: 

    def __init__(self):
        try:
            self.repository= Repository("bjj", "techniques")
        except:
            self.repository= FakeRepository()
    def GetAll(self):
        data= self.repository.GetAll()
        return {"entries":data}

    def Filter(self, value):
        q={"name": { "$regex":'{}'.format(value), '$options' : 'i' }}
        data= self.repository.Filter(q)
        return {"entries":data}

    def Post(self, t):
        return self.repository.Post(t)
     