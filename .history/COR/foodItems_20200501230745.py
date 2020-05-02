class Fooddon(object):
    def __init__(self, nxt): 
         self._nxt = nxt 
    def handle(self, request): 
        handled = self.processRequest(request) 
        if not handled: 
            self._nxt.handle(request) 
    def processRequest(self, request):   
        raise NotImplementedError

class Grains(Fooddon):
    def processRequest(self, request):
        if request=="g":
            request='Grain'
            print(f'Enter the type of {request} you want to select :')
            grain=["Wheat","Rice","Potato","Onion"]
            print(f'Enter the quantity of {grain[2]} in kgs :')
            return True

class Products(Fooddon):
    def processRequest(self, request):
        if request=="p":
            request='Product'
            print(f'Enter the type of {request} of product you want to select :')
            products=["Cheese","BreadPack","Pasta","Sphagetti"]
            print(f'Enter the number of {products[1]} packets :')
            return True

class Fruit_Items(Fooddon):
    def processRequest(self, request):
        if request=="i":
            request='Fruit'
            print(f'Enter the type of {request} packet you want to select :')    
            items=["Apple Packets","Banana Packets"]       
            print(f'Enter the number of {items[1]} packets :')
            return True

class User: 
   
    def __init__(self): 
        initial = None  
        self.handler = Grains(Products(Fruit_Items((initial))))
    def agent(self, user_request):   
        for request in user_request: 
            self.handler.handle(request) 
  
"""main method"""
  
if __name__ == "__main__": 
    user = User() 
    choose_request="g"
    requests = list(choose_request)
    user.agent(requests) 



    



