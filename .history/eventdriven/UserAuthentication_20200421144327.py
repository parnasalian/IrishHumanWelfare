from app import Login
from database.dbconn import Database_connection
from dao.dao import *
from flask import render_template
class Mediator:
    def login(self,username_form,password_form):
        donationsDictionary = {}
        donationsDictionary = DataBase.retrieveDonations()       #gets list of donations options from the database
        dbPassword = DataBase.getPasswordForLogin(username_form) #gets password from the db
        if password_form  == dbPassword:
            return render_template("index.html",donationsDictionary = donationsDictionary)     
        else:
            return render_template("login.html")  

    def register():
        pass

class UserChoice:
    def __init__(self): 
        self.mediator = Mediator()
    def optForLogin(self,username_form,password_form):
        return self.mediator.login(username_form,password_form)
    
    def optForRegister():
        self.mediator.register()