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
        self.place.getplace()
        self.category.getcategory()
        self.mode.getmode()
        

# Client
if __name__ == '__main__':
    facade = Facade()
    facade.start_clothes()
    print("Donation Successful")