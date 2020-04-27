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
        self.cur.execute("SELECT * FROM donation_location") 
        for row in self.cur.fetchall():
            locations.append(row[1])
        return locations
    
    def getPasswordForLogin(self,username_form):
        self.cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if self.cur.fetchone()[0]:
            self.cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in self.cur.fetchall():
                dbPassword = row[0]
        return dbPassword