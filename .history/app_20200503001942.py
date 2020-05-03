from flask import Flask, session, render_template, request, session, g, redirect, url_for
import os, random
import mysql.connector
from database.dbconn import Database_connection
from donations.donations import Donations
from money_donation.money_donation import Payments,CreditCardCommand,NetBankingCommand,Money_Donation
from food_donation.food_donation import *
from eventdriven.UserAuthentication import *
from dao.dao import *
from paymentAuthentication.concreteInterceptor import *
from paymentAuthentication.dispatcher import *
from paymentAuthentication.concreteFramework import *
from paymentAuthentication.Interceptor_contextObject import *
from food_donation.foodItems import *
from pipe_filter.partyLeftOver import *
app = Flask(__name__)
dbcon=DataBase.dbconn()


class Login:
    @app.route("/login",methods = ['POST','GET'])
    def login():
        return render_template("login.html")

    @app.route("/back",methods = ['POST'])
    def back():
        donationsDictionary = {}
        db = DataBase()
        donationsDictionary = db.retrieveDonations()
        return render_template("index.html",donationsDictionary = donationsDictionary)
    
    @app.route("/processLogin",methods = ['POST','GET'])    #Event producer
    def processLogin():
        if request.method == "POST":
            username_form  = request.form['username']
            password_form  = request.form['password']
        login = UserChoice()    # Instance of Event Channel
        return login.optForLogin(username_form,password_form)  #Passing the credentials along with the event to the event channel.
    
    @app.route("/logout",methods = ['POST','GET'])
    def logout():
        session.pop("username", None)
        return redirect(url_for("login"))
        
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
        userDetailsDictionary = {'name':custName,'email':custEmail,'password':custPassword,'address':custAddress,'phonenumber':custPhoneNumber}
        register = UserChoice()
        return register.optForRegister(userDetailsDictionary)
        
        
        
  
class ChooseDonation:
    @app.route('/get_donations', methods = ['POST','GET'])
    def get_donations():
        if request.method == "POST":
            userSelection = request.args.get('user_selection')
            print("Check",userSelection)
        df = Donations()
        donation = df.get_donation_type(userSelection)
        don = donation()
        return don.get_donation()

class FoodDonation:
    @app.route('/get_foodDonation_type', methods = ['POST','GET'])
    def get_foodDonation_type():
        if request.method == "POST":
            foodDonationType = request.args.get('type')
        print("User selected ",foodDonationType)
        ftype = eval(foodDonationType)  #creating the instance of visitor class
        food = Fooddonation()
        return food.accept(ftype)

    @app.route('/processFoodItems',methods = ["POST","GET"])
    def processFoodItems():
        if request.method == "POST":
            choice = request.args.get('type')
        print("User chose",choice)
        user = User() 
        requests = []
        requests.append(choice)
        return user.agent(requests) 


    @app.route('/getCreditCardPaymentPage',methods = ["POST","GET"])
    def getCreditCardPaymentPage():
        return render_template('creditCardPayment.html')
    
    @app.route('/processPaymentForFood', methods = ['POST','GET'])
    def processPaymentForFood():
        if request.method == 'POST':
            cardNumber = request.form['cardnumber']
        print(cardNumber)
        concreteinterceptor = ConcreteInterceptor2()
        dispatcher = Dispatcher2()
        dispatcher.registerInterceptors(concreteinterceptor)
        concreteframework = ConcreteFramework2()
        concreteframework.processtransaction(cardNumber)
        return concreteframework.notifyDispatcher()

    @app.route('/processFoodDonation',methods = ['POST','GET'])
    def processFoodDonation():
        if request.method == "POST":
            foodItem = request.form['item']
            quantity = request.form['quantity']
            location = request.form['location']
            mode = request.form['mode_']
        db = DataBase()
        db.donateFoodDetails(foodItem,quantity,location,mode)
        return render_template("success.html")
    
    @app.route('/processPartyLeftover', methods = ['POST','GET'])
    def processPartyLeftover():
        if request.method == "POST":
            location = request.form['location']
            category = request.form['category']
            mode = request.form['mode_']
        leftovers = Fooddonate()
        leftovers.location(location)
        leftovers.category(category)
        leftovers.mode(mode)
        return render_template("success.html")
class MoneyDonation:
    @app.route('/processMoneyDonation', methods = ['POST','GET'])
    def processMoneyDonation():
        if request.method == "POST":
            donation_amount = request.form['amount']
            donation_frequency = request.form['frequency']
            payment_method = request.form['paymentmethod']
        db = DataBase()
        db.addCashDetailsToDB(donation_amount,donation_frequency,payment_method)
        # The Payments is the Reciever
        payment = Payments()

        # Create Commands
        payViaCredit = CreditCardCommand(payment)
        payViaNetBanking = NetBankingCommand(payment)

        # Register the commands with the invoker
        moneyDonation = Money_Donation()
        moneyDonation.register("Credit/Debit", payViaCredit)
        moneyDonation.register("Netbanking", payViaNetBanking)

        # Execute the commands that are registered on the Invoker
        return moneyDonation.execute(payment_method)
    
    @app.route('/completeMoneyDonation',methods = ['POST','GET'])
    def completeMoneyDonation():
        return render_template('success.html')
    
  
class HomePage:
    @app.route("/index", methods = ['POST','GET'])
    def indexPage():
        return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='127.0.0.1', port=5000, threaded=True)