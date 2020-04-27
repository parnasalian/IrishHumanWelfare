"""has methods to obtain info from concrete framework - accessor methods
control behaviour of concrete framework  - mutator methods

Used by concrete interceptors for the above functionalities

"""
class ContextObject(object):

    def _init_(self,cardNumber):
        self.cardNumber = cardNumber
    

    def getCardNumber():
        return self.cardNumber
        
