"""has methods to obtain info from concrete framework - accessor methods
control behaviour of concrete framework  - mutator methods

Used by concrete interceptors for the above functionalities

"""
class ContextObject(object):
    def __init__(self,cardNumber):
        self.cardNumber = cardNumber
        print(self.cardNumber)

    def getCardNumber(self):
        print("Inside getCardNumber",self.cardNumber)
        return self.cardNumber
        
