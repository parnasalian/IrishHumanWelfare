class place:
    def getplace(self):
        val = input("Enter the place:")
        print(val)

class category:
    def getcategory(self):
        val = input("Enter the Category:")
        print(val)

class mode:
    def getmode(self): 
        val = input("Enter the Mode:")
        print(val)

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
        return clothes_dictionary

        
