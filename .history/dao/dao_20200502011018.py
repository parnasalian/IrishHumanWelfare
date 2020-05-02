from database.dbconn import Database_connection
import mysql.connector
from flask import session
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

    def getCategories(self):
        categories = []
        self.cur.execute("SELECT * FROM clothes_category") 
        for row in self.cur.fetchall():
            categories.append(row[1])
        return categories
    
    def getModes(self):
        mode = []
        self.cur.execute("SELECT * FROM mode_of_transport") 
        for row in self.cur.fetchall():
            mode.append(row[1])
        return mode
    
    def getPasswordForLogin(self,username_form):
        user_dictionary = {}
        self.cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if self.cur.fetchone()[0]:
            self.cur.execute("SELECT * FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in self.cur.fetchall():
                username = row[0]
                email = row[1]
                phonenumber = row[2]
                dbPassword = row[3]
                address = row[4]
        user_dictionary = {'user_name':username,'user_email':email,'user_phnumber':phonenumber,'password':dbPassword,'user_address':address}
        return user_dictionary

    def insertUserDataInDB(self,userdetails_dictionary):
        query = "INSERT INTO user_info(username,email,phone,user_password,address) VALUES(%s,%s,%s,%s,%s)"
        args = (userdetails_dictionary['name'], userdetails_dictionary['email'], userdetails_dictionary['phonenumber'], userdetails_dictionary['password'], userdetails_dictionary['address'])
        self.cur.execute(query,args)
        self.dbcon.commit()
        pass

    def getFoodDonationType(self):
        dictionary = {}
        self.cur.execute("SELECT * FROM food_donation_types") 
        for row in self.cur.fetchall():
            food_donation_type = row[0]
            keyword = row[1]
            dictionary = {**dictionary,**{food_donation_type:keyword}}
        return dictionary
    
    def getFoodItems(self):
        foodItemsList = []
        self.cur.execute("SELECT * FROM food_types") 
        for row in self.cur.fetchall():
            food_type = row[0]
            if food_type not in foodItemsList:
                foodItemsList.append(food_type)
        return foodItemsList
    
    def getGrains(self,request):
        grains = []
        self.cur.execute("SELECT * FROM food_types WHERE foodCategory = %s;", [request]) 
        for row in self.cur.fetchall():
            grain = row[1]
            grains.append(grain)
        return grains

    def getProducts(self,request):
        products = []
        self.cur.execute("SELECT * FROM food_types WHERE foodCategory = %s;", [request]) 
        for row in self.cur.fetchall():
            product = row[1]
            products.append(product)
        return products

    def getFruits(self,request):
        fruits = []
        self.cur.execute("SELECT * FROM food_types WHERE foodCategory = %s;", [request]) 
        for row in self.cur.fetchall():
            fruit = row[1]
            fruits.append(fruit)
        return fruits

    def donateFoodDetails(self,foodItem,quantity,location,mode):
        query = "INSERT INTO home_food_donation(donar,donar_email,donar_address,donar_phonenumber,donation_item,donation_quantity,location, donation_mode) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (session['username'], session['email'], session['address'], session['phonenumber'],foodItem,quantity,location,mode)
        self.cur.execute(query,args)
        self.dbcon.commit()


    def addCashDetailsToDB(self,donation_amount,donation_frequency,payment_method):
        query = "INSERT INTO money_donation(donar,donar_email,donar_address,donar_phonenumber,donation_amount,donation_frequency,payment_method) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        args = (session['username'], session['email'], session['address'], session['phonenumber'], donation_amount,donation_frequency,payment_method)
        self.cur.execute(query,args)
        self.dbcon.commit()
        pass


