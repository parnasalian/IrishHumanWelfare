from database.dbconn import Database_connection
from dao.dao import *

class place:
    def __init__(self):
        self.db = DataBase()
    def getplace(self):
        locations = []
        locations = self.db.getLocations()
        return locations

class category:
    def getcategory(self):
        categories = []
        test = place()
        categories = test.db.getCategories()
        return categories

class mode:
    def getmode(self): 
        mode = []
        test = place()
        mode = test.db.getModes()
        return mode

# Facade
class Facade:
    def __init__(self):
        self.place = place()
        self.category = category()
        self.mode = mode()

    def getDropdownDetails(self):
        dropdown_dictionary = {}
        location = []
        category = []
        mode = []

        location = self.place.getplace()
        category = self.category.getcategory()
        mode = self.mode.getmode()
        dropdown_dictionary = {'location':location,'category':category,'mode':mode}
        print("Clothes Dictionary",dropdown_dictionary)
        return dropdown_dictionary

        
