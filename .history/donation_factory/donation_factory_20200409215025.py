from abc import ABCMeta, abstractstaticmethod

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def donationPeriod():
        pass
        #Donation Interface

class CashDonation(IDonation):
    def donationPeriod():
        return render_template('cash_donation.html')

class DonationFactory():
    @app.route('/get_donation_type', methods = ['POST','GET'])
    def get_donation_type(donationType):
        try:
            if donationType == userSelection:
                return eval(userSelection)
            raise AssertionError("Donation not selected")
        except AssertionError as _e:
            print(_e)


