class Fooddon(object):
    def __init__(self, nxt): 
         self._nxt = nxt 
    def handle(self, request): 
        handled = self.processRequest(request) 
        if not handled: 
            self._nxt.handle(request) 
  
    def processRequest(self, request):   
        print('Please select the type of food')

class Grains(Fooddon):
    def processRequest(self, request):
        value=input('Add Element: ')
        quantity=2
        grain=set(["Wheat","Rice","Potato","Onion"])
        set.add(value)
        print(f'Enter the quantity in kgs : {quantity}')
        return True

class Products(Fooddon):
    def processRequest(self, request):
        value=input('Add Element: ')
        no_of_items=0
        items=set(["Cheese","BreadPack","Pasta","Sphagetti"])
        set.add(value)
        print(f'Enter the quantity : {no_of_items}')
        return True

class Fruit_Items(Fooddon):
    def processRequest(self, request):
        value=input('Add Element: ')
        no_of_items=0
        items=set(["Apple Packets","Banana Packets"])
        set.add(value)
        print(f'Enter the quantity : {no_of_items}')
        return True

class DefaultHandler(Fooddon):
    def processRequest(self, request): 
        other_item=dict()
        print(f'Enter the other item you want to donate: {other_item}')
class User: 
   
    def __init__(self): 
        initial = None  
        self.handler = Grains(Products(Fruit_Items(DefaultHandler(initial))))  
    def agent(self, user_request):   
        for request in user_request: 
            self.handler.handle(request) 
  
"""main method"""
  
if __name__ == "__main__": 
    user = User() 
    choose_request = "Typeoffood"
    requests = list(choose_request) 
    user.agent(requests) 
