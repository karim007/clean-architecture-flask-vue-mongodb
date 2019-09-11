from pymongo import MongoClient
import simplejson as json
import os
class DataBase:
      def __init__(self):
                  self.client = MongoClient("mngodb://your db here ")
      def getContext(self):
                  return self.client

class Repository:
  def __init__(self, db, collection):
            self.collection=DataBase().getContext()[db][collection]

  def GetAll(self):
            return self.collection.find({})



  def Filter(self, query):
            return self.collection.find(query)

  def Post(self, item):
        return self.collection.insert_one(item).inserted_id






class FakeRepository:
      def Filter(self, query):
            path = os.path.dirname(os.path.abspath(__file__))
            print(path)
            my_file = os.path.join(path, 'FakeData.json')
            with open(my_file) as json_file:
                  data = json.load(json_file)
                  data=list(data)
                  if(query):
                        data = filter(lambda item:  query["name"]["$regex"] in item["name"] , data)
                  return data
