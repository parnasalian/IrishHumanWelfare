from abc import ABCMeta, abstractstaticmethod
from flask import render_template
#Reciever
class Payments:
    def credit_card_payment(self):
        print("What the hell!")
        return render_template('creditCardPayment.html')
    def net_banking_payment(self):
        return render_template('netBankingPayment.html')

#ICommand Interface
class ICommand(metaclass=ABCMeta):  #metaclass=ABCMeta - This helps to enforce interface rules on a class
    @abstractstaticmethod
    def execute():
        """All commands will implement this method of the Icommand interface"""
        pass

#Command1 - credit
class CreditCardCommand(ICommand):
    def __init__(self,payment):
        self._payment = payment
    def execute(self):
        print("Hit bro!!")
        return self._payment.credit_card_payment()

#Command2 - netbanking
class NetBankingCommand(ICommand):
    def __init__(self,payment):
        self._payment = payment
    def execute(self):
       return self._payment.net_banking_payment()

#Invoker - 
class Cash_Donation:
    def __init__(self):
        self._commands = {}
    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            return self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

