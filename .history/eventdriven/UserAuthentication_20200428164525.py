from app import Login
from database.dbconn import Database_connection
from dao.dao import *
from flask import render_template, redirect, url_for
class EventProcessor(object):
    def __init__(self):
        self.db = DataBase()

    def login(self,username_form,password_form):
        donationsDictionary = {}   
        donationsDictionary = db.retrieveDonations()       #gets list of donations options from the database
        dbPassword = db.getPasswordForLogin(username_form) #gets password from the db
        if password_form  == dbPassword:
            return render_template("index.html",donationsDictionary = donationsDictionary)     
        else:
            return render_template("login.html")  

    def register(self,userdetails_dictionary):
        reg = self.db.insertUserDataInDB(userdetails_dictionary)
        donationsDictionary = {}
        donationsDictionary = self.db.retrieveDonations()
        return render_template("index.html",donationsDictionary = donationsDictionary)
        

class UserChoice:   #Acts as a event channel
    def __init__(self): 
        self.eventProcessor = EventProcessor() #Initiated our processor for processing data for the event.
    def optForLogin(self,username_form,password_form):
        return self.eventProcessor.login(username_form,password_form)
    
    def optForRegister(self,userdetails_dictionary):
        return self.eventProcessor.register(userdetails_dictionary)