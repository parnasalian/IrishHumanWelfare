from abc import ABCMeta, abstractstaticmethod

#Reciever
class Payments:
    def credit_card_payment(self):
        return render_template("creditCardPayment.html")
    def net_banking_payment(self):
        return render_template("netBankingPayment.html")

#ICommand Interface
class ICommand(metaclass=ABCMeta):  #metaclass=ABCMeta - This helps to enforce interface rules on a class
    @abstractstaticmethod
    def execute():
        "All the commands will implement this method of the Icommand interface"

#Command - credit
class CreditCardCommand(ICommand):
    def __init__(self,payment):
        self._payment = payment
    def execute(self):
       self._payment.credit_card_payment()

#Command - netbanking
class NetBankingCommand(ICommand):
    def __init__(self,payment):
        self._payment = payment
    def execute(self):
       self._payment.net_banking_payment()

#Invoker - cash_donation

#Client - app.py