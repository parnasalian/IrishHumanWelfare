from abc import ABCMeta, abstractstaticmethod
import sys
from flask import render_template
from clothes_donation.clothes_donation import Facade
from database.dbconn import Database_connection

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_donation():
        pass
        #Donation Interface

class CashDonation(IDonation):
    def get_donation():
        return render_template('cash_donation.html')

class FoodDonation(IDonation):
    def get_donation():
        dictionary = {}
        dbcon=Database_connection.dbconn()
        cur=dbcon.cursor()
        cur.execute("SELECT * FROM food_donation_types") # FETCH THE HASHED PASSWORD
        for row in cur.fetchall():
            food_donation_type = row[0]
            keyword = row[1]
            dictionary = {**dictionary,**{food_donation_type:keyword}}
        return dictionary
        return render_template('food_donation.html',dictionary = dictionary)

class ClothesDonation(IDonation):
    def get_donation():
        clothes_dictionary = {}
        facade = Facade()
        clothes_dictionary = facade.start_clothes()
        print("Inside factory",clothes_dictionary)
        return render_template('clothes_donation.html',clothes_dictionary = clothes_dictionary)

class DonationFactory():
    def get_donation_type(donationType):
        print("Donation",donationType)
        #donation_dictionary = {"donation_type":donationType}
        return eval(donationType) 
  

