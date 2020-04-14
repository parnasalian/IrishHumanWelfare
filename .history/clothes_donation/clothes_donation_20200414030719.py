from database.dbconn import Database_connection

class place:
    def getplace(self):
        locations = []
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM donation_location") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            locations.append(row[1])
        print(locations)
        return locations

class category:
    def getcategory(self):
        categories = []
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM clothes_category") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            categories.append(row[1])
        print(categories)
        return categories

class mode:
    def getmode(self): 
        mode = []
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM mode_of_transport") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            mode.append(row[1])
        print(mode)
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

        
