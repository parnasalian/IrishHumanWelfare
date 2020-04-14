from database.dbconn import Database_connection

class place:
    def getplace(self):
        locations = []
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM donation_location") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            locations.append(row[1])

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

        
