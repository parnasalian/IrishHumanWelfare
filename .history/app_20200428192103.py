from flask import Flask, session, render_template, request, session, g, redirect, url_for
import os, random
import mysql.connector
from database.dbconn import Database_connection
from donation_factory.donation_factory import DonationFactory
from cash_donation.cash_donation import Payments,CreditCardCommand,NetBankingCommand,Cash_Donation
from food_donation.food_donation import *
from eventdriven.UserAuthentication import *
from dao.dao import *
from interceptorPattern.concreteInterceptor import *
from interceptorPattern.dispatcher import *
from interceptorPattern.concreteFramework import *
app = Flask(__name__)
dbcon=DataBase.dbconn()


class Login:
    @app.route("/login",methods = ['POST','GET'])
    def login():
        return render_template("login.html")

    @app.route("/back",methods = ['POST','GET'])
    def back():
        donationsDictionary = {}
        donationsDictionary = DataBase.retrieveDonations()
        return render_template("index.html",donationsDictionary = donationsDictionary)
    
    @app.route("/processLogin",methods = ['POST','GET'])    #Event producer
    def processLogin():
        if request.method == "POST":
            username_form  = request.form['username']
            password_form  = request.form['password']
        login = UserChoice()    # Instance of Event Channel
        return login.optForLogin(username_form,password_form)  #Passing the credentials along with the event to the event channel.
        
class Register:
    @app.route("/register") 
    def register():
        return render_template("register.html")

    @app.route("/processRegistration",methods = ['POST','GET'])
    def processRegistration():
        userDetailsDictionary = {}
        if request.method == "POST":
            print("Enter!!")
            custName = request.form['Username']
            print(custName)
            custEmail = request.form['Email']
            custPassword = request.form['Password']
            custAddress = request.form['Address']
            custPhoneNumber = request.form['PhoneNumber']
        session['username'] = custName
        session['email'] = custEmail
        session['phonenumber'] = custPhoneNumber
        session['address'] = custAddress
        userDetailsDictionary = {'name':custName,'email':custEmail,'password':custPassword,'address':custAddress,'phonenumber':custPhoneNumber}
        register = UserChoice()
        return register.optForRegister(userDetailsDictionary)
        
        
        
  
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
    
    @app.route('/processPaymentForFood', methods = ['POST','GET'])
    def processPaymentForFood():
        if request.method == 'POST':
            cardNumber = request.form['CardNumber']
        print(cardNumber)
        concreteinterceptor = ConcreteInterceptor()
        dispatcher = Dispatcher()
        dispatcher.registerInterceptors(concreteinterceptor)
        concreteframework = ConcreteFramework()
        concreteframework.processtransaction(cardNumber)
        return concreteframework.notifyDispatcher()

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
        
      
class HomePage:
    @app.route("/index", methods = ['POST','GET'])
    def indexPage():
        return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)