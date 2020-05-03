from flask import render_template
from clothes_donation.clothes_donation import *
class FoodItems(object):
    def __init__(self, nxt): 
         self._nxt = nxt 
    def handle(self, request): 
        print("Request in handle",request)
        handled = self.processRequest(request) 
        if not handled: 
            return self._nxt.handle(request) 
        else:
            return handled
    def processRequest(self, request):   
        pass

class Grains(Fooddon):
    def processRequest(self, request):
        if request=="Grains":
            db = DataBase()
            dropdown_dictionary = {}
            grainsList = []
            grainsList = db.getGrains(request)
            facade = Facade()
            dropdown_dictionary = facade.getDropdownDetails()
            print("Inside factory",dropdown_dictionary)
            return render_template('grains.html',dropdown_dictionary = dropdown_dictionary,grainsList = grainsList)

class Products(Fooddon):
    def processRequest(self, request):
        if request=="Products":
            db = DataBase()
            dropdown_dictionary = {}
            productsList = []
            productsList = db.getProducts(request)
            facade = Facade()
            dropdown_dictionary = facade.getDropdownDetails()
            print("Inside factory",dropdown_dictionary)
            return render_template('products.html',dropdown_dictionary = dropdown_dictionary,productsList = productsList)


class Fruit_Items(Fooddon):
    def processRequest(self, request):
        if request=="Fruits":
            db = DataBase()
            dropdown_dictionary = {}
            fruitsList = []
            fruitsList = db.getFruits(request)
            facade = Facade()
            dropdown_dictionary = facade.getDropdownDetails()
            print("Inside factory",dropdown_dictionary)
            return render_template('fruits.html',dropdown_dictionary = dropdown_dictionary,fruitsList = fruitsList)

class User: 
   
    def __init__(self): 
        initial = None  
        self.handler = Grains(Products(Fruit_Items((initial))))
    def agent(self, user_request):   
        for request in user_request: 
            print("Request in agent",request)
            return self.handler.handle(request) 
  




    



