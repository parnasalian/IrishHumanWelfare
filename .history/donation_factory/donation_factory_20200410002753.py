from abc import ABCMeta, abstractstaticmethod
import sys

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def donationPeriod():
        pass
        #Donation Interface

class CashDonation(IDonation):
    def donationPeriod():
        return render_template('cash_donation.html')

class FoodDonation(IDonation):
    def donationPeriod():
        return render_template('food_donation.html')

class ClothesDonation(IDonation):
    def donationPeriod():
        return render_template('clothes_donation.html')

class DonationFactory():
    def get_donation_type(donationType):
        print("Donation",donationType)
        donation_dictionary = {"donation_type":donationType}
        return donation_dictionary["donation_type"]()
  

