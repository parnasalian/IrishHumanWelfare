from flask import render_template
from clothes_donation.clothes_donation import *

class Fooddonation(object):

    def accept(self,visitor):
        #Interface to accept a visitor
        return visitor.visit(self)

    def gets_buy_food():
        foodItemsList = {}
        db = DataBase()
        foodItemsList = db.getFoodItems()
        return render_template("buyFood.html",foodItemsList = foodItemsList)
    def gets_donate_food():
        dropdown_dictionary = {}
        facade = Facade()
        dropdown_dictionary = facade.getDropdownDetails()
        print("Inside factory",dropdown_dictionary)
        return render_template("donateFood.html",dropdown_dictionary = dropdown_dictionary)
    def gets_party_leftovers():
        dropdown_dictionary = {}
        facade = Facade()
        dropdown_dictionary = facade.getDropdownDetails()
        print("Inside factory",dropdown_dictionary)
        return render_template("partyLeftovers.html",dropdown_dictionary = dropdown_dictionary)



class Visitor(object):
    pass

class BuyFood(Visitor):
    def visit(self):
        return Fooddonation.gets_buy_food()

class Donate_Food(Visitor):
    def visit(self):
        return Fooddonation.gets_donate_food()

class Party_leftovers(Visitor):
    def visit(self):
        return Fooddonation.gets_party_leftovers()   





