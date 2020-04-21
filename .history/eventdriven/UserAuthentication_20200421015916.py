from app import Login
from database.dbconn import Database_connection
from flask import render_template
class Mediator:
    def login(self,username_form,password_form):
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        donationsDictionary = {}
        donationsDictionary = Login.retrieveDonations()
        cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form  == row[0]:
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