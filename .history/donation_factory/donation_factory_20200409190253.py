from abc import ABCMeta, abstractstaticmethod

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def donationPeriod():
        #Donation Interface

class CashDonation(IDonation):
    def donationPeriod():
        return render_template('cash_donation.html')

class DonationFactory():
    @app.route('/get_donation_type', methods = ['POST','GET'])
    def get_donation_type(donationType):
        if request.method == "POST":
            userSelection = request.args.get('user_selection')
        try:
            if donationType == userSelection:
                return eval(userSelection).donationPeriod()
            raise AssertionError("Chair not found"):
        except AssertionError as _e:
            print(_e)


