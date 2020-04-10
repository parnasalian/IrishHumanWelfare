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
            userSelection = request.form['userSelection']
        try:
            if donationType == userSelection:
                return 

