from abc import ABCMeta, abstractstaticmethod
import sys
from flask import render_template
from clothes_donation.clothes_donation import Facade
from database.dbconn import Database_connection
from dao.dao import *

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_donation():
        pass
        #Donation Interface

class CashDonation(IDonation):
    def get_donation():
        return render_template('cash_donation.html')

class FoodDonation(IDonation):
    def __init__(self):
        self.db = DataBase()

    def get_donation(self):
        dictionary = {}
        dictionary = self.db.getFoodDonationType()
        return render_template('food_donation.html',dictionary = dictionary)

class ClothesDonation(IDonation):
    def get_donation():
        clothes_dictionary = {}
        facade = Facade()
        clothes_dictionary = facade.start_clothes()
        print("Inside factory",clothes_dictionary)
        return render_template('clothes_donation.html',clothes_dictionary = clothes_dictionary)

class DonationFactory:
    def get_donation_type(self,donationType):
        print("Donation",donationType)
        #donation_dictionary = {"donation_type":donationType}
        return ast.literal_eval(donationType) 
  

