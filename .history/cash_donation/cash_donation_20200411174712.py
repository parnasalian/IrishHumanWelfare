from abc import ABCMeta, abstractstaticmethod

#Reciever - Payments

#ICommand Interface
#metaclass=ABCMeta - This helps to enforce interface rules on a class
class ICommand(metaclass=ABCMeta)  
#Command - credit
#Command - netbanking
#Invoker - cash_donation
#Client - app.py