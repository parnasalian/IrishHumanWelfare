from database.dbconn import Database_connection
from dao.dao import *

class place:
    def getplace(self):
        locations = []
        db = DataBase()
        locations = db.getLocations()
        return locations

class category:
    def getcategory(self):
        categories = []
        categories = DataBase.getCategories()
        return categories

class mode:
    def getmode(self): 
        mode = []
        mode = DataBase.getModes()
        return mode

# Facade
class Facade:
    def __init__(self):
        self.place = place()
        self.category = category()
        self.mode = mode()

    def start_clothes(self):
        clothes_dictionary = {}
        location = []
        category = []
        mode = []

        location = self.place.getplace()
        category = self.category.getcategory()
        mode = self.mode.getmode()
        clothes_dictionary = {'location':location,'category':category,'mode':mode}
        print("Clothes Dictionary",clothes_dictionary)
        return clothes_dictionary

        
