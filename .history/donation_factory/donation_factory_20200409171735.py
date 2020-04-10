from abc import ABCMeta, abstractstaticmethod

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def donationPeriod():
        #Donation Interface

class CashDonation(IDonation):
    def donationPeriod():
        return render_template('cash_donation.html')
