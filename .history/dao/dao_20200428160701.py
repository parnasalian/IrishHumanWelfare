from database.dbconn import Database_connection
import mysql.connector
class DataBase:
    def __init__(self):
        self.dbcon=Database_connection.dbconn()
        self.cur=self.dbcon.cursor()
    
    def dbconn():
        mydb = mysql.connector.connect(
        user='bc5865edd7a83b',
        password='c1f43ffa',
        host='eu-cdbr-west-02.cleardb.net',
        port=3306,
        database='heroku_dffdac2c032f563')
        return mydb

    def retrieveDonations(self):
        dictionary = {} 
        self.cur.execute("SELECT * FROM DonationType") # FETCH THE HASHED PASSWORD
        for row in self.cur.fetchall():
            donation_type = row[1]
            keyword = row[2]
            dictionary = {**dictionary,**{donation_type:keyword}}
        return dictionary

    def getLocations(self):
        locations = []
        self.cur.execute("SELECT * FROM donation_location") 
        for row in self.cur.fetchall():
            locations.append(row[1])
        return locations

    def getCategories():
        categories = []
        self.cur.execute("SELECT * FROM clothes_category") 
        for row in self.cur.fetchall():
            categories.append(row[1])
        return categories
    
    def getModes():
        mode = []
        self.cur.execute("SELECT * FROM mode_of_transport") 
        for row in self.cur.fetchall():
            mode.append(row[1])
        return mode
    
    def getPasswordForLogin(self,username_form):
        self.cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if self.cur.fetchone()[0]:
            self.cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in self.cur.fetchall():
                dbPassword = row[0]
        return dbPassword

    def insertUserDataInDB(userdetails_dictionary):
        query = "INSERT INTO user_info(username,email,phone,user_password,address) VALUES(%s,%s,%s,%s,%s)"
        args = (userdetails_dictionary.name, userdetails_dictionary.email,  userdetails_dictionary.password, userdetails_dictionary.address, userdetails_dictionary.phonenumber)
        self.cur.execute(query,args)
        self.dbcon.commit()
        print("Row inserted...")

    def getFoodDonationType():
        self.cur.execute("SELECT * FROM food_donation_types") 
        for row in self.cur.fetchall():
            food_donation_type = row[0]
            keyword = row[1]
            dictionary = {**dictionary,**{food_donation_type:keyword}}
        return dictionary