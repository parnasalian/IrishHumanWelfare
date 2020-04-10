from abc import ABCMeta, abstractstaticmethod

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_donationType():
        #Donation Interface