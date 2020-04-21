from app import Login
from database.dbconn import Database_connection
from dao.dao import *
from flask import render_template
class EventProcessor(object):
    def login(self,username_form,password_form):
        donationsDictionary = {}
        db = DataBase()
        donationsDictionary = db.retrieveDonations()       #gets list of donations options from the database
        dbPassword = db.getPasswordForLogin(username_form) #gets password from the db
        if password_form  == dbPassword:
            return render_template("index.html",donationsDictionary = donationsDictionary)     
        else:
            return render_template("login.html")  

    def register():
        pass

class UserChoice:
    def __init__(self): 
        self.eventProcessor = EventProcessor()
    def optForLogin(self,username_form,password_form):
        return self.eventProcessor.login(username_form,password_form)
    
    def optForRegister():
        self.eventProcessor.register()