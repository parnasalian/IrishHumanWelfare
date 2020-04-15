class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        visitor.visit(self)

    def buy_food():
    def donate_food():
    def party_leftovers():

class Visitor(object):
    def visit(self,fooddon):

class BuyFood(Fooddon):
    def processRequest(self, request):
        quantity=0
        print(f'Enter the quantity in kgs : {quantity}')
        return True

class Donate_Food(Fooddon):
    def processRequest(self, request):
        no_of_items=0
        print(f'Enter the quantity : {no_of_items}')
        return True

class Party_leftovers(Fooddon):
    def processRequest(self, request):
        no_of_items=0
        print(f'Enter the quantity : {no_of_items}')
        return True        

class DefaultHandler(Fooddon):
    def processRequest(self, request): 
        other_item=0
        print(f'Enter the other item you want to donate: {other_item}')
class User: 
   
    def __init__(self): 
        initial = None  
        self.handler = BuyFood(Donate_Food(Party_leftovers(DefaultHandler(initial)))) 
    def agent(self, user_request):   
        for request in user_request: 
            self.handler.handle(request) 
  
"""main method"""
  
if __name__ == "__main__": 
    user = User() 
    string = "Typeoffood"
    requests = list(string) 
    user.agent(requests) 
