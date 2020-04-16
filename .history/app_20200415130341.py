from flask import Flask, session, render_template, request, session, g, redirect, url_for
import os, random
import mysql.connector
from database.dbconn import Database_connection
from donation_factory.donation_factory import DonationFactory
from cash_donation.cash_donation import Payments,CreditCardCommand,NetBankingCommand,Cash_Donation
from food_donation.food_donation import *
app = Flask(__name__)
dbcon=Database_connection.dbconn()


class Login:
    @app.route("/login",methods = ['POST','GET'])
    def login():
        return render_template("login.html")
    
    def retrieveDonations():
        dictionary = {}
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM DonationType") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            donation_type = row[1]
            keyword = row[2]
            dictionary = {**dictionary,**{donation_type:keyword}}
        return dictionary
    
    @app.route("/processLogin",methods = ['POST','GET'])
    def processLogin():
        donationsDictionary = {}
        donationsDictionary = Login.retrieveDonations()
        print("Donation dictionary",donationsDictionary)
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        username_form  = request.form['username']
        password_form  = request.form['password'] 
        cur.execute("SELECT COUNT(1) FROM user_info WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT user_password FROM user_info WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form  == row[0]:
                    session['user'] = username_form
                    print("PASSWORD is correct...")
                    return redirect(url_for('indexPage',donationsDictionary = donationsDictionary)  )   
                else:
                    return render_template("login.html")  
        return render_template("login.html")

class ChooseDonation:
    @app.route('/get_donation_type', methods = ['POST','GET'])
    def get_donation_type():
        if request.method == "POST":
            userSelection = request.args.get('user_selection')
            print("Check",userSelection)
        donation = DonationFactory.get_donation_type(userSelection)

        return donation.get_donation()

class FoodDonation:
    @app.route('/get_foodDonation_type', methods = ['POST','GET'])
    def get_foodDonation_type():
        if request.method == "POST":
            foodDonationType = request.args.get('type')
        print("User selected ",foodDonationType)
        ftype = eval(foodDonationType)  #creating the instance of visitor class
        food = Fooddonation()
        return food.accept(ftype)

class CashDonation:
    @app.route('/processCashDonation', methods = ['POST','GET'])
    def processCashDonation():
        if request.method == "POST":
            donar_name = request.form['name']
            donar_address = request.form['address']
            donar_phone_number = request.form['PhoneNumber']
            donation_amount = request.form['amount']
            donation_frequency = request.form['frequency']
            payment_method = request.form['paymentmethod']
            print("Payment method", payment_method)
        
        # The Payments is the Reciever
        payment = Payments()

        # Create Commands
        payViaCredit = CreditCardCommand(payment)
        payViaNetBanking = NetBankingCommand(payment)

        # Register the commands with the invoker
        cashDonation = Cash_Donation()
        cashDonation.register("Credit/Debit", payViaCredit)
        cashDonation.register("Netbanking", payViaNetBanking)

        # Execute the commands that are registered on the Invoker
        return cashDonation.execute(payment_method)
        



class Register:
    @app.route("/register") 
    def register():
        return render_template("register.html")


    @app.route("/processRegistration",methods = ['POST','GET'])
    def processRegistration():
        if request.method == "POST":
            print("Enter!!")
            custName = request.form['Username']
            print(custName)
            custEmail = request.form['Email']
            custPassword = request.form['Password']
            custAddress = request.form['Address']
            custPhoneNumber = request.form['PhoneNumber']
        print(dbcon)
        cur=dbcon.cursor()
        query = "INSERT INTO user_info(username,email,phone,user_password,address) VALUES(%s,%s,%s,%s,%s)"
        args = (custName, custEmail,  custPhoneNumber, custPassword, custAddress)
        cur.execute(query,args)
        dbcon.commit()
        print("Row inserted...")
        return redirect(url_for('indexPage'))
      
class HomePage:
    @app.route("/index", methods = ['POST','GET'])
    def indexPage():
        donationsDictionary = {}
        donationsDictionary = request.args.get('donationsDictionary')
        print("Dictionary is ",donationsDictionary)
        return render_template("index.html",donationsDictionary = donationsDictionary)



if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)