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
    def get_donation_type():
        if request.method == "POST":
            userSelection = request.args.get('user_selection')
            return eval(userSelection).donationPeriod()
            

