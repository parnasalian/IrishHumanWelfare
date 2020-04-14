from abc import ABCMeta, abstractstaticmethod
import sys
from flask import render_template
from clothes_donation.clothes_donation import Facade

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
        return render_template('food_donation.html')

class ClothesDonation(IDonation):
    def get_donation():
        facade = Facade()
        facade.start_clothes()
        return render_template('clothes_donation.html')

class DonationFactory():
    def get_donation_type(donationType):
        print("Donation",donationType)
        #donation_dictionary = {"donation_type":donationType}
        return eval(donationType)
  

